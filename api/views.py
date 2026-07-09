import time
import uuid
import base64
import requests
from rest_framework.decorators import api_view, permission_classes
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.mail import send_mail
from django.conf import settings
@api_view(['POST'])
def register_user(request):
    username = request.data.get('username')
    email = request.data.get('email')
    first_name = request.data.get('first_name')
    last_name = request.data.get('last_name')
    password = request.data.get('password')

    if not username or not password:
        return Response({"error": "Username and password required"}, status=400)

    if User.objects.filter(username=username).exists():
        return Response({"error": "Username exists"}, status=400)

    if email and User.objects.filter(email=email).exists():
        return Response({"error": "Email exists"}, status=400)

    # Create user
    user = User.objects.create_user(
        username=username,
        email=email,
        password=password,
        first_name=first_name,
        last_name=last_name
    )
    # Generate JWT token
    refresh = RefreshToken.for_user(user)

    return Response({
        "message": "User created successfully",
        "user": {
            "id": user.id,
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
        },
        "token": str(refresh.access_token)
    }, status=201)








from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken


@api_view(['POST'])
def login_user(request):
    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(username=username, password=password)

    if user is None:
        return Response({"error": "Invalid credentials"}, status=400)
    # Generate JWT token
    token = RefreshToken.for_user(user)

    return Response({
        "access": str(token.access_token),
        "refresh": str(token),
        "user": {
            "id": user.id,
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
        }
    })
# =========================
# PROFILE
# =========================
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_profile(request):
    user = request.user

    return Response({
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "first_name": user.first_name,
        "last_name": user.last_name,
    })


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

# =========================
# PAYSTACK INIT
# =========================
@api_view(['POST'])
def initialize_payment(request):
    email = request.data.get("email")
    amount = request.data.get("amount")

    if not email or not amount:
        return Response({"error": "Email and amount required"}, status=400)

    try:
        amount = int(amount) * 100
    except:
        return Response({"error": "Invalid amount"}, status=400)

    url = "https://api.paystack.co/transaction/initialize"

    headers = {
        "Authorization": f"Bearer {settings.PAYSTACK_SECRET_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "email": email,
        "amount": amount,
    }

    response = requests.post(url, json=payload, headers=headers)

    return Response(response.json(), status=response.status_code)


# =========================
# PAYSTACK BALANCE
# =========================
import requests
@api_view(['GET'])
def paystack_balance(request):
    url = "https://api.paystack.co/balance"

    headers = {
        "Authorization": f"Bearer {settings.PAYSTACK_SECRET_KEY}"
    }

    response = requests.get(url, headers=headers)

    return Response(response.json(), status=response.status_code)







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