import time
import uuid
import base64
import requests
from rest_framework.decorators import api_view, permission_classes
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.mail import send_mail
from django.utils import timezone
from django.utils import timezone


from notifications.services import (
    send_welcome_notification,
    send_login_notification,
)


# =====================================
# REGISTER
# =====================================

@api_view(["POST"])
def register_user(request):

    fullname = request.data.get("first_name")
    phone = request.data.get("phone")
    email = request.data.get("email")
    password = request.data.get("password")
    referral = request.data.get("referral", "")

    if not fullname or not phone or not email or not password:
        return Response(
            {
                "error": "Full name, phone, email and password are required."
            },
            status=400,
        )

    if User.objects.filter(username=phone).exists():
        return Response(
            {
                "error": "Phone number already exists."
            },
            status=400,
        )

    if User.objects.filter(email=email).exists():
        return Response(
            {
                "error": "Email already exists."
            },
            status=400,
        )

    names = fullname.strip().split(" ", 1)

    first_name = names[0]
    last_name = names[1] if len(names) > 1 else ""

    user = User.objects.create_user(
        username=phone,
        email=email,
        password=password,
        first_name=first_name,
        last_name=last_name,
    )

    try:
        send_welcome_notification(user)
    except Exception as e:
        print("WELCOME NOTIFICATION:", e)

    refresh = RefreshToken.for_user(user)

    return Response(
        {
            "message": "Account created successfully",

            "access": str(refresh.access_token),
            "refresh": str(refresh),

            "user": {
                "id": user.id,
                "phone": user.username,
                "email": user.email,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "referral": referral,
            },
        },
        status=201,
    )


# =====================================
# LOGIN
# Phone OR Email
# =====================================

@api_view(["POST"])
def login_user(request):

    username = request.data.get("username")
    password = request.data.get("password")
    device = request.data.get("device", "Flutter Mobile")

    if not username or not password:
        return Response(
            {
                "error": "Phone/Email and password are required."
            },
            status=400,
        )

    user = None

    if "@" in username:

        try:
            user_obj = User.objects.get(email=username)

            user = authenticate(
                username=user_obj.username,
                password=password,
            )

        except User.DoesNotExist:
            pass

    else:

        user = authenticate(
            username=username,
            password=password,
        )

    if user is None:
        return Response(
            {
                "error": "Invalid phone/email or password."
            },
            status=400,
        )

    try:

        send_login_notification(
            user=user,
            device=device,
            ip=request.META.get("REMOTE_ADDR"),
            login_time=timezone.now(),
        )

    except Exception as e:
        print("LOGIN NOTIFICATION:", e)

    refresh = RefreshToken.for_user(user)

    return Response(
        {
            "access": str(refresh.access_token),
            "refresh": str(refresh),

            "user": {
                "id": user.id,
                "phone": user.username,
                "email": user.email,
                "first_name": user.first_name,
                "last_name": user.last_name,
            },
        }
    )


# =====================================
# PROFILE
# =====================================

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def user_profile(request):

    user = request.user

    fullname = f"{user.first_name} {user.last_name}".strip()

    return Response(
        {
            "id": user.id,
            "phone": user.username,
            "email": user.email,
            "fullname": fullname,
            "first_name": user.first_name,
            "last_name": user.last_name,
        }
    )

# =========================
# LOGOUT
# =========================
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_user(request):
    return Response({"message": "Logout successful"})


# =========================
# FORGOT PASSWORD (FIXED SAFE)
# =========================
@api_view(['POST'])
def forgot_password(request):
    email = request.data.get('email')

    if not email:
        return Response({"error": "Email required"}, status=400)

    user = User.objects.filter(email=email).first()

    if not user:
        return Response({"error": "Email not found"}, status=404)

    return Response({
        "message": "User found",
        "username": user.username
    })


# =========================
# RESET PASSWORD (FIXED SAFE)
# =========================
@api_view(['POST'])
def reset_password(request):
    email = request.data.get('email')
    new_password = request.data.get('new_password')

    if not email or not new_password:
        return Response({"error": "Required fields missing"}, status=400)

    user = User.objects.filter(email=email).first()

    if not user:
        return Response({"error": "User not found"}, status=404)

    user.set_password(new_password)
    user.save()

    return Response({"message": "Password reset successful"})


# =========================
# GOOGLE LOGIN (PLACEHOLDER)
# =========================
from google.oauth2 import id_token
from google.auth.transport import requests
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken


GOOGLE_CLIENT_ID = "YOUR_WEB_CLIENT_ID.apps.googleusercontent.com"


@api_view(["POST"])
def google_login(request):
    token = request.data.get("id_token")

    if not token:
        return Response({"error": "Missing ID token"}, status=400)

    try:
        info = id_token.verify_oauth2_token(
            token,
            requests.Request(),
            GOOGLE_CLIENT_ID,
        )

        email = info["email"]
        first_name = info.get("given_name", "")
        last_name = info.get("family_name", "")
        username = email.split("@")[0]

        user, created = User.objects.get_or_create(
            email=email,
            defaults={
                "username": username,
                "first_name": first_name,
                "last_name": last_name,
            },
        )

        refresh = RefreshToken.for_user(user)

        return Response({
            "access": str(refresh.access_token),
            "refresh": str(refresh),
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "first_name": user.first_name,
                "last_name": user.last_name,
            },
        })

    except Exception:
        return Response({"error": "Invalid Google token"}, status=400)

# # =========================
# # PAYSTACK INIT
# # =========================
# @api_view(['POST'])
# def initialize_payment(request):
#     email = request.data.get("email")
#     amount = request.data.get("amount")

#     if not email or not amount:
#         return Response({"error": "Email and amount required"}, status=400)

#     try:
#         amount = int(amount) * 100
#     except:
#         return Response({"error": "Invalid amount"}, status=400)

#     url = "https://api.paystack.co/transaction/initialize"

#     headers = {
#         "Authorization": f"Bearer {settings.PAYSTACK_SECRET_KEY}",
#         "Content-Type": "application/json",
#     }

#     payload = {
#         "email": email,
#         "amount": amount,
#     }

#     response = requests.post(url, json=payload, headers=headers)

#     return Response(response.json(), status=response.status_code)


# # =========================
# # PAYSTACK BALANCE
# # =========================
# import requests
# @api_view(['GET'])
# def paystack_balance(request):
#     url = "https://api.paystack.co/balance"

#     headers = {
#         "Authorization": f"Bearer {settings.PAYSTACK_SECRET_KEY}"
#     }

#     response = requests.get(url, headers=headers)

#     return Response(response.json(), status=response.status_code)







# variation

import base64

def vtpass_auth():
    credentials = f"{settings.VTPASS_EMAIL}:{settings.VTPASS_PASSWORD}"
    token = base64.b64encode(credentials.encode()).decode()

    return {
        "Authorization": f"Basic {token}",
        "Content-Type": "application/json"
    }






# @api_view(['GET'])
# def service_variations(request):
#     service_id = request.GET.get("serviceID")

#     if not service_id:
#         return Response({"error": "serviceID is required"}, status=400)

#     headers = {
#         "api-key": settings.VTPASS_API_KEY,
#         "public-key": settings.VTPASS_PUBLIC_KEY,
#     }

#     response = requests.get(
#         "https://sandbox.vtpass.com/api/service-variations",
#         params={"serviceID": service_id},
#         headers=headers
#     )

#     data = response.json()

#     variations = data.get("content", {}).get("variations", [])

#     PROFIT = 1  # backend-only

#     clean = []

#     for item in variations:
#         try:
#             base = float(item.get("variation_amount", 0))
#         except:
#             base = 0

#         clean.append({
#             "variation_code": item.get("variation_code"),
#             "name": item.get("name"),
#             "price": base + PROFIT   # ONLY final price shown
#         })

#     return Response({
#         "response_description": data.get("response_description"),
#         "content": {
#             "serviceID": service_id,
#             "variations": clean
#         }
#     })




# # # webbook
# from decimal import Decimal
# import requests
# from django.conf import settings
# from rest_framework.decorators import api_view
# from rest_framework.response import Response

# from paystack.models import Wallet, Transaction, VariationCode
# @api_view(["GET"])
# def service_variations(request):
#     service_id = request.GET.get("serviceID")

#     if not service_id:
#         return Response(
#             {"error": "serviceID is required"},
#             status=400
#         )

#     headers = {
#         "api-key": settings.VTPASS_API_KEY,
#         "public-key": settings.VTPASS_PUBLIC_KEY,
#     }

#     response = requests.get(
#         "https://sandbox.vtpass.com/api/service-variations",
#         params={"serviceID": service_id},
#         headers=headers,
#         timeout=30,
#     )

#     data = response.json()

#     variations = data.get("content", {}).get("variations", [])

#     PROFIT = Decimal("1.00")

#     clean = []

#     for item in variations:

#         variation_code = item.get("variation_code")
#         name = item.get("name")

#         try:
#             amount = Decimal(
#                 str(item.get("variation_amount", 0))
#             )
#         except Exception:
#             amount = Decimal("0.00")

#         # Save or update in database
#         VariationCode.objects.update_or_create(
#             variation_code=variation_code,
#             defaults={
#                 "service_id": service_id,
#                 "name": name,
#                 "amount": amount,
#                 "fixed_price": True,
#                 "active": True,
#             },
#         )

#         clean.append({
#             "variation_code": variation_code,
#             "name": name,
#             "price": float(amount + PROFIT),
#         })

#     return Response({
#         "response_description": data.get("response_description"),
#         "content": {
#             "serviceID": service_id,
#             "variations": clean,
#         },
#     })



from decimal import Decimal
import requests

from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response

from paystack.models import VariationCode


@api_view(["GET"])
def service_variations(request):

    service_id = request.GET.get("serviceID")


    if not service_id:

        return Response(
            {
                "error":"serviceID is required"
            },
            status=400
        )



    headers = {

        "api-key": settings.VTPASS_API_KEY,

        "public-key": settings.VTPASS_PUBLIC_KEY,

    }



    response = requests.get(

        "https://sandbox.vtpass.com/api/service-variations",

        params={
            "serviceID":service_id
        },

        headers=headers,

        timeout=30,

    )



    data = response.json()



    variations = (
        data
        .get("content", {})
        .get("variations", [])
    )



    PROFIT = Decimal("1.00")

    clean = []



    for item in variations:


        variation_code = item.get(
            "variation_code"
        )


        name = item.get(
            "name"
        )



        try:

            amount = Decimal(
                str(
                    item.get(
                        "variation_amount",
                        0
                    )
                )
            )

        except:

            amount = Decimal("0.00")



        VariationCode.objects.update_or_create(

            variation_code=variation_code,

            defaults={

                "service": service_id,

                "name": name,

                "amount": amount,

                "fixed_price": True,

                "active": True,

            },

        )



        clean.append({

            "variation_code":variation_code,

            "name":name,

            "price":str(
                amount + PROFIT
            ),

        })



    return Response({

        "response_description":data.get(
            "response_description"
        ),

        "content":{

            "serviceID":service_id,

            "variations":clean,

        }

    })





from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["GET"])
def app_stats(request):
    return Response({
        "total_users": User.objects.count(),
        "app_link": "https://your-app-link.com"
    })










# forgetten reset_password
import random

from django.core.mail import send_mail
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.contrib.auth.models import User
from .models import PasswordResetOTP


@api_view(["POST"])
def forgot_password(request):

    email = request.data.get("email")


    # Check email input
    if not email:
        return Response(
            {
                "error": "Email required"
            },
            status=400
        )


    # Clean email
    email = email.strip().lower()


    # Find user email
    user = User.objects.filter(
        email__iexact=email
    ).first()


    if not user:
        return Response(
            {
                "error": "Email not found"
            },
            status=404
        )


    # Remove previous OTP
    PasswordResetOTP.objects.filter(
        user=user
    ).delete()


    # Create OTP
    otp = str(
        random.randint(100000, 999999)
    )


    # Save OTP
    PasswordResetOTP.objects.create(
        user=user,
        otp=otp
    )


    print("PASSWORD RESET OTP:", otp)


    try:

        sent = send_mail(

    subject="Mass Data Password Reset OTP",

    message=f"""
Hello {user.username},

Your Mass Data password reset OTP is:

{otp}

This OTP expires in 10 minutes.

Do not share this code with anyone.
""",

    from_email=settings.DEFAULT_FROM_EMAIL,

    recipient_list=[
        user.email
    ],

    fail_silently=False,
)

        print("EMAIL SENT:", sent)


        if sent == 0:
            return Response(
                {
                    "error": "Email was not sent"
                },
                status=500
            )


    except Exception as e:

        print("EMAIL ERROR:", str(e))


        return Response(
            {
                "error": "Failed to send OTP",
                "details": str(e)
            },
            status=500
        )


    return Response(
        {
            "message": "OTP sent successfully"
        }
    )

import random

from django.conf import settings
from django.core.mail import send_mail

from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.contrib.auth.models import User

from .models import PasswordResetOTP


from django.utils import timezone

@api_view(["POST"])
def verify_otp(request):

    email = request.data.get("email")
    otp_code = request.data.get("otp")


    if not email or not otp_code:
        return Response(
            {
                "error": "Email and OTP are required"
            },
            status=400
        )


    user = User.objects.filter(
        email=email
    ).first()


    if not user:
        return Response(
            {
                "error": "User not found"
            },
            status=404
        )


    reset = PasswordResetOTP.objects.filter(
        user=user,
        otp=otp_code
    ).first()


    if not reset:
        return Response(
            {
                "error": "Invalid OTP"
            },
            status=400
        )


    if reset.is_expired():

        reset.delete()

        return Response(
            {
                "error": "OTP expired"
            },
            status=400
        )


    reset.verified = True
    reset.save()


    return Response(
        {
            "message": "OTP verified successfully"
        }
    )




@api_view(["POST"])
def reset_password(request):

    email = request.data.get("email")
    new_password = request.data.get("new_password")


    if not email or not new_password:
        return Response(
            {
                "error": "Email and new password are required"
            },
            status=400
        )


    user = User.objects.filter(
        email=email
    ).first()


    if not user:
        return Response(
            {
                "error": "User not found"
            },
            status=404
        )


    reset = PasswordResetOTP.objects.filter(
        user=user,
        verified=True
    ).first()


    if not reset:
        return Response(
            {
                "error": "Please verify OTP first"
            },
            status=400
        )


    if reset.is_expired():

        reset.delete()

        return Response(
            {
                "error": "OTP expired"
            },
            status=400
        )


    user.set_password(new_password)
    user.save()


    # remove OTP after successful reset
    reset.delete()


    return Response(
        {
            "message": "Password reset successful"
        }
    )




