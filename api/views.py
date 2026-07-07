# import time
# import uuid
# import base64
# import requests
# from rest_framework.decorators import api_view, permission_classes
# from django.conf import settings
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# from rest_framework_simplejwt.tokens import RefreshToken
# from django.contrib.auth.models import User
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework_simplejwt.tokens import RefreshToken



# @api_view(['POST'])
# def register_user(request):
#     username = request.data.get('username')
#     email = request.data.get('email')
#     first_name = request.data.get('first_name')
#     last_name = request.data.get('last_name')
#     password = request.data.get('password')

#     if not username or not password:
#         return Response({"error": "Username and password required"}, status=400)

#     if User.objects.filter(username=username).exists():
#         return Response({"error": "Username exists"}, status=400)

#     if email and User.objects.filter(email=email).exists():
#         return Response({"error": "Email exists"}, status=400)

#     user = User.objects.create_user(
#         username=username,
#         email=email,
#         password=password,
#         first_name=first_name,
#         last_name=last_name
#     )

#     # 🔥 GENERATE TOKEN (THIS FIXES YOUR 401 ISSUE)
#     refresh = RefreshToken.for_user(user)

#     return Response({
#         "message": "User created",
#         "user": {
#             "id": user.id,
#             "username": user.username,
#             "first_name": user.first_name,
#             "last_name": user.last_name,
#         },
#         "token": str(refresh.access_token)   # ✅ IMPORTANT
#     }, status=201)
# # =========================
# # LOGIN (JWT)
# # =========================
# @api_view(['POST'])
# def login_user(request):
#     username = request.data.get("username")
#     password = request.data.get("password")

#     user = authenticate(username=username, password=password)

#     if user is None:
#         return Response({"error": "Invalid credentials"}, status=400)

#     token = RefreshToken.for_user(user)

#     return Response({
#         "access": str(token.access_token),
#         "refresh": str(token),
#         "user": {
#             "id": user.id,
#             "username": user.username,
#             "first_name": user.first_name,
#             "last_name": user.last_name,
#         }
#     })


# # =========================
# # PROFILE
# # =========================
# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def user_profile(request):
#     user = request.user

#     return Response({
#         "id": user.id,
#         "username": user.username,
#         "email": user.email,
#         "first_name": user.first_name,
#         "last_name": user.last_name,
#     })


# # =========================
# # LOGOUT
# # =========================
# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def logout_user(request):
#     return Response({"message": "Logout successful"})


# # =========================
# # FORGOT PASSWORD (FIXED SAFE)
# # =========================
# @api_view(['POST'])
# def forgot_password(request):
#     email = request.data.get('email')

#     if not email:
#         return Response({"error": "Email required"}, status=400)

#     user = User.objects.filter(email=email).first()

#     if not user:
#         return Response({"error": "Email not found"}, status=404)

#     return Response({
#         "message": "User found",
#         "username": user.username
#     })


# # =========================
# # RESET PASSWORD (FIXED SAFE)
# # =========================
# @api_view(['POST'])
# def reset_password(request):
#     email = request.data.get('email')
#     new_password = request.data.get('new_password')

#     if not email or not new_password:
#         return Response({"error": "Required fields missing"}, status=400)

#     user = User.objects.filter(email=email).first()

#     if not user:
#         return Response({"error": "User not found"}, status=404)

#     user.set_password(new_password)
#     user.save()

#     return Response({"message": "Password reset successful"})


# # =========================
# # GOOGLE LOGIN (PLACEHOLDER)
# # =========================
# @api_view(['POST'])
# def google_login(request):
#     return Response({"message": "Google login not implemented yet"})


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



# import requests
# import uuid
# import random
# import string
# import time
# from datetime import datetime

# from django.conf import settings
# from rest_framework.decorators import api_view
# from rest_framework.response import Response


# def vtpass_headers():
#     print("API KEY:", settings.VTPASS_API_KEY)
#     print("SECRET KEY:", settings.VTPASS_SECRET_KEY)

#     return {
#         "Content-Type": "application/json",
#         "api-key": settings.VTPASS_API_KEY,
#         "secret-key": settings.VTPASS_SECRET_KEY,
#     }

# # =========================
# # REQUEST ID GENERATOR
# # =========================
# def generate_request_id():
#     now = datetime.now().strftime("%Y%m%d%H%M")
#     rand = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
#     return f"{now}{rand}"


# # =========================
# # SAFE REQUEST HELPER
# # =========================
# def vtpass_post(url, payload):
#     try:
#         res = requests.post(url, json=payload, headers=vtpass_headers(), timeout=30)

#         try:
#             return res.json(), res.status_code
#         except Exception:
#             return {"error": "Invalid VTpass response", "raw": res.text}, 500

#     except requests.exceptions.RequestException as e:
#         return {"error": "Network error", "details": str(e)}, 503


# # =========================
# # AIRTIME
# # =========================
# @api_view(['POST'])
# def buy_airtime(request):

#     service_map = {
#         "mtn": "mtn",
#         "airtel": "airtel",
#         "glo": "glo",
#         "9mobile": "9mobile"
#     }

#     network = request.data.get("network")
#     amount = request.data.get("amount")
#     phone = request.data.get("phone")

#     if not network or not amount or not phone:
#         return Response({"error": "network, amount, phone required"}, status=400)

#     service_id = service_map.get(network.lower())

#     if not service_id:
#         return Response({"error": "Invalid network"}, status=400)

#     payload = {
#         "request_id": str(uuid.uuid4()),
#         "serviceID": service_id,
#         "amount": amount,
#         "phone": phone
#     }

#     data, status = vtpass_post("https://sandbox.vtpass.com/api/pay", payload)
#     return Response(data, status=status)



# @api_view(['POST'])
# def buy_data(request):

#     network_map = {
#         "mtn": "mtn-data",
#         "airtel": "airtel-data",
#         "glo": "glo-data",
#         "9mobile": "etisalat-data"
#     }

#     network = request.data.get("network")
#     phone = request.data.get("phone")
#     variation_code = request.data.get("variation_code")
#     amount = request.data.get("amount")

#     if not network or not phone or not variation_code:
#         return Response({"error": "network, phone, variation_code required"}, status=400)

#     service_id = network_map.get(network.lower())

#     if not service_id:
#         return Response({"error": "Invalid network"}, status=400)

#     payload = {
#         "request_id": generate_request_id(),
#         "serviceID": service_id,
#         "billersCode": phone,
#         "variation_code": variation_code,
#         "amount": amount,
#         "phone": phone,
#     }

#     data, status = vtpass_post(
#         "https://sandbox.vtpass.com/api/pay",
#         payload
#     )

#     return Response(data, status=status)

# # =========================
# # GOTV
# # =========================
# import uuid
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# import requests


# def vtpass_get(url):
#     res = requests.get(url)
#     return res.json(), res.status_code

# import requests



# @api_view(['POST'])
# def buy_gotv(request):

#     billers_code = request.data.get("billersCode")
#     variation_code = request.data.get("variation_code")
#     phone = request.data.get("phone")
#     subscription_type = request.data.get("subscription_type", "change")

#     if not billers_code:
#         return Response({"error": "billersCode is required"}, status=400)

#     if not variation_code:
#         return Response({"error": "variation_code is required"}, status=400)

#     if not phone:
#         return Response({"error": "phone is required"}, status=400)

#     # 🔥 GET VARIATIONS
#     vtpass_variations, _ = vtpass_get(
#         "https://sandbox.vtpass.com/api/service-variations?serviceID=gotv"
#     )

#     real_price = None

#     for v in vtpass_variations["content"]["variations"]:
#         if v["variation_code"] == variation_code:
#             real_price = float(v["variation_amount"])

#     if real_price is None:
#         return Response({"error": "Invalid variation"}, status=400)

#     # 🔥 YOUR PROFIT (HIDDEN)
#     profit = 50
#     selling_price = real_price + profit

#     payload = {
#         "request_id": str(uuid.uuid4()),
#         "serviceID": "gotv",
#         "billersCode": billers_code,
#         "variation_code": variation_code,
#         "amount": real_price,  # VTpass only sees real price
#         "phone": phone,
#         "subscription_type": subscription_type,
#     }

#     data, http_status = vtpass_post(
#         "https://sandbox.vtpass.com/api/pay",
#         payload
#     )

#     # 🔥 STORE PROFIT (REAL WAY)
#     if data.get("code") == "000":
#         transaction = data["content"]["transactions"]

#         # ⚠️ THIS IS ONLY RESPONSE MODIFICATION
#         transaction["user_paid"] = selling_price
#         transaction["profit"] = profit

#         # 👉 BEST PRACTICE: SAVE TO DATABASE HERE
#         # Transaction.objects.create(...)

#     return Response(data, status=http_status)







# # =========================
# # STARTIMES
# # =========================
# import uuid
# import requests
# from rest_framework.decorators import api_view
# from rest_framework.response import Response


# import uuid
# import requests

# from rest_framework.decorators import api_view
# from rest_framework.response import Response

# import uuid
# import requests

# from django.conf import settings
# from rest_framework.decorators import api_view
# from rest_framework.response import Response


# @api_view(['POST'])
# def buy_startimes(request):

#     billers_code = request.data.get("billersCode")
#     variation_code = request.data.get("variation_code")
#     phone = request.data.get("phone")

#     # VALIDATION
#     if not billers_code:
#         return Response(
#             {"error": "billersCode is required"},
#             status=400
#         )

#     if not variation_code:
#         return Response(
#             {"error": "variation_code is required"},
#             status=400
#         )

#     if not phone:
#         return Response(
#             {"error": "phone is required"},
#             status=400
#         )

#     # GET STARTIMES VARIATIONS
#     try:
#         variation_response = requests.get(
#             "https://sandbox.vtpass.com/api/service-variations",
#             params={"serviceID": "startimes"},
#             headers={
#                 "api-key": settings.VTPASS_API_KEY,
#                 "public-key": settings.VTPASS_PUBLIC_KEY,
#             },
#             timeout=20,
#         )

#         data_variations = variation_response.json()

#     except Exception as e:
#         return Response({
#             "error": "Failed to fetch Startimes variations",
#             "details": str(e)
#         }, status=500)

#     # FIND REAL PRICE
#     real_price = None

#     for item in data_variations.get("content", {}).get("variations", []):
#         if item.get("variation_code") == variation_code:
#             real_price = float(item.get("variation_amount", 0))
#             break

#     if real_price is None:
#         return Response({
#             "error": "Invalid variation_code"
#         }, status=400)

#     # PROFIT
#     profit = 50
#     selling_price = real_price + profit

#     # PAYMENT PAYLOAD
#     payload = {
#         "request_id": str(uuid.uuid4()),
#         "serviceID": "startimes",
#         "billersCode": billers_code,
#         "variation_code": variation_code,
#         "amount": real_price,
#         "phone": phone,
#     }

#     try:
#         vtpass_response = requests.post(
#             "https://sandbox.vtpass.com/api/pay",
#             json=payload,
#             headers={
#                 "api-key": settings.VTPASS_API_KEY,
#                 "secret-key": settings.VTPASS_SECRET_KEY,
#                 "Content-Type": "application/json",
#                 "Accept": "application/json",
#             },
#             timeout=20,
#         )

#         data = vtpass_response.json()

#     except Exception as e:
#         return Response({
#             "error": "VTpass payment failed",
#             "details": str(e)
#         }, status=500)

#     # SUCCESS
#     if data.get("code") == "000":
#         transaction = data.get("content", {}).get("transactions", {})

#         transaction["user_paid"] = selling_price
#         transaction["profit"] = profit

#     return Response(
#         data,
#         status=vtpass_response.status_code
#     )
# # =========================
# # ELECTRICITY VERIFY
# # =========================
# @api_view(['POST'])
# def verify_meter(request):

#     payload = {
#         "billersCode": request.data.get("billersCode"),
#         "serviceID": request.data.get("serviceID"),
#         "type": request.data.get("type"),
#     }

#     try:
#         res = requests.post(
#             "https://vtpass.com/api/merchant-verify",
#             json=payload,
#             headers=vtpass_headers(),
#             timeout=30
#         )
#         return Response(res.json())
#     except Exception as e:
#         return Response({"error": str(e)}, status=503)






# # buy_showmax


# import uuid
# import requests

# from rest_framework.decorators import api_view
# from rest_framework.response import Response


# @api_view(['POST'])
# def buy_showmax(request):

#     billers_code = request.data.get("billersCode")
#     variation_code = request.data.get("variation_code")

#     if not billers_code:
#         return Response(
#             {"error": "billersCode is required"},
#             status=400,
#         )

#     if not variation_code:
#         return Response(
#             {"error": "variation_code is required"},
#             status=400,
#         )

#     # ==========================
#     # GET SHOWMAX VARIATIONS
#     # ==========================
#     try:
#         res = requests.get(
#             "https://sandbox.vtpass.com/api/service-variations",
#             params={"serviceID": "showmax"},
#             timeout=20,
#         )

#         data_variations = res.json()

#     except Exception as e:
#         return Response({
#             "error": "Failed to fetch Showmax plans",
#             "details": str(e)
#         }, status=500)

#     # ==========================
#     # FIND REAL PRICE
#     # ==========================
#     real_price = None

#     for v in data_variations.get("content", {}).get("variations", []):
#         if v.get("variation_code") == variation_code:
#             real_price = float(v.get("variation_amount", 0))
#             break

#     if real_price is None:
#         return Response({
#             "error": "Invalid variation_code"
#         }, status=400)

#     # ==========================
#     # YOUR PROFIT
#     # ==========================
#     profit = 50
#     selling_price = real_price + profit

#     # ==========================
#     # PAYMENT PAYLOAD
#     # ==========================
#     payload = {
#         "request_id": str(uuid.uuid4()),
#         "serviceID": "showmax",
#         "billersCode": billers_code,
#         "variation_code": variation_code,
#         "amount": real_price,
#     }

#     try:
#         vtpass_response = requests.post(
#             "https://sandbox.vtpass.com/api/pay",
#             json=payload,
#             timeout=20,
#             headers={
#                 "Content-Type": "application/json",
#                 "Accept": "application/json",
#             }
#         )

#         data = vtpass_response.json()

#     except Exception as e:
#         return Response({
#             "error": "VTpass payment failed",
#             "details": str(e)
#         }, status=500)

#     # ==========================
#     # SUCCESS
#     # ==========================
#     if data.get("code") == "000":
#         transaction = data.get("content", {}).get("transactions", {})

#         transaction["user_paid"] = selling_price
#         transaction["profit"] = profit

#     return Response(
#         data,
#         status=vtpass_response.status_code,
#     )


# # =========================
# # ELECTRICITY BUY
# # =========================
# @api_view(['POST'])
# def buy_electricity(request):

#     payload = {
#         "request_id": str(int(time.time())),
#         "serviceID": request.data.get("service_id"),
#         "billersCode": request.data.get("meter_number"),
#         "variation_code": request.data.get("meter_type"),
#         "amount": request.data.get("amount"),
#         "phone": request.data.get("phone")
#     }

#     data, status = vtpass_post("https://vtpass.com/api/pay", payload)
#     return Response(data, status=status)






# # Education



# # waec_variations



# @api_view(['GET'])
# def waec_variations(request):
#     res = requests.get(
#         "https://sandbox.vtpass.com/api/service-variations?serviceID=waec-registration",
#         headers=vtpass_headers()
#     )
#     return Response(res.json())



# # buy_waec_registration


# @api_view(['POST'])
# def buy_waec_registration(request):

#     payload = {
#         "request_id": generate_request_id(),
#         "serviceID": "waec-registration",
#         "variation_code": request.data.get("variation_code"),
#         "quantity": request.data.get("quantity", 1),
#         "phone": request.data.get("phone"),
#     }

#     data, status_code = vtpass_post(
#         "https://sandbox.vtpass.com/api/pay",
#         payload
#     )

#     return Response(data, status=status_code)



# # requery_transaction

# @api_view(['POST'])
# def requery_transaction(request):

#     payload = {
#         "request_id": request.data.get("request_id")
#     }

#     data, status_code = vtpass_post(
#         "https://sandbox.vtpass.com/api/requery",
#         payload
#     )

#     return Response(data, status=status_code)

# # result checker


# @api_view(['GET'])
# def waec_result_variations(request):
#     url = "https://sandbox.vtpass.com/api/service-variations?serviceID=waec"
#     res = requests.get(url, headers=vtpass_headers())
#     return Response(res.json())




# @api_view(['POST'])
# def buy_waec_result_pin(request):

#     payload = {
#         "request_id": generate_request_id(),
#         "serviceID": "waec",
#         "variation_code": request.data.get("variation_code"),
#         "quantity": request.data.get("quantity", 1),
#         "phone": request.data.get("phone"),
#     }

#     data, status = vtpass_post(
#         "https://sandbox.vtpass.com/api/pay",
#         payload
#     )

#     return Response(data, status=status)




# @api_view(['POST'])
# def waec_result_requery(request):

#     payload = {
#         "request_id": request.data.get("request_id")
#     }

#     data, status = vtpass_post(
#         "https://sandbox.vtpass.com/api/requery",
#         payload
#     )

#     return Response(data, status=status)




#     # Jamb
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# import requests

# # make sure these exist in your project
# # from .utils import vtpass_headers, vtpass_post, generate_request_id


# # =========================
# # JAMB VARIATIONS (GET)
# # =========================
# @api_view(['GET'])
# def jamb_variations(request):
#     url = "https://sandbox.vtpass.com/api/service-variations?serviceID=jamb"
#     res = requests.get(url, headers=vtpass_headers())
#     return Response(res.json())


# # =========================
# # VERIFY / REQUERY (POST)
# # =========================
# @api_view(['POST'])
# def jamb_requery(request):

#     payload = {
#         "request_id": request.data.get("request_id")
#     }

#     data, status = vtpass_post(
#         "https://sandbox.vtpass.com/api/requery",
#         payload
#     )

#     return Response(data, status=status)


# # =========================
# # BUY JAMB PIN (POST)
# # =========================
# @api_view(['POST'])
# def buy_jamb_pin(request):

#     payload = {
#         "request_id": generate_request_id(),
#         "serviceID": "jamb",
#         "variation_code": request.data.get("variation_code"),
#         "billersCode": request.data.get("billersCode", "0123456789"),
#         "phone": request.data.get("phone")
#     }

#     data, status = vtpass_post(
#         "https://sandbox.vtpass.com/api/pay",
#         payload
#     )

#     return Response(data, status=status)





# import base64

# def vtpass_auth():
#     credentials = f"{settings.VTPASS_EMAIL}:{settings.VTPASS_PASSWORD}"
#     token = base64.b64encode(credentials.encode()).decode()

#     return {
#         "Authorization": f"Basic {token}",
#         "Content-Type": "application/json"
#     }






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

#     PROFIT = 100  # backend-only

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


# # buy_gotv




# import time
# import uuid
# import base64
# import requests
# from rest_framework.decorators import api_view, permission_classes
# from django.conf import settings
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# from rest_framework_simplejwt.tokens import RefreshToken
# from django.contrib.auth.models import User
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework_simplejwt.tokens import RefreshToken



# @api_view(['POST'])
# def register_user(request):
#     username = request.data.get('username')
#     email = request.data.get('email')
#     first_name = request.data.get('first_name')
#     last_name = request.data.get('last_name')
#     password = request.data.get('password')

#     if not username or not password:
#         return Response({"error": "Username and password required"}, status=400)

#     if User.objects.filter(username=username).exists():
#         return Response({"error": "Username exists"}, status=400)

#     if email and User.objects.filter(email=email).exists():
#         return Response({"error": "Email exists"}, status=400)

#     user = User.objects.create_user(
#         username=username,
#         email=email,
#         password=password,
#         first_name=first_name,
#         last_name=last_name
#     )

#     # 🔥 GENERATE TOKEN (THIS FIXES YOUR 401 ISSUE)
#     refresh = RefreshToken.for_user(user)

#     return Response({
#         "message": "User created",
#         "user": {
#             "id": user.id,
#             "username": user.username,
#             "first_name": user.first_name,
#             "last_name": user.last_name,
#         },
#         "token": str(refresh.access_token)   # ✅ IMPORTANT
#     }, status=201)
# # =========================
# # LOGIN (JWT)
# # =========================
# @api_view(['POST'])
# def login_user(request):
#     username = request.data.get("username")
#     password = request.data.get("password")

#     user = authenticate(username=username, password=password)

#     if user is None:
#         return Response({"error": "Invalid credentials"}, status=400)

#     token = RefreshToken.for_user(user)

#     return Response({
#         "access": str(token.access_token),
#         "refresh": str(token),
#         "user": {
#             "id": user.id,
#             "username": user.username,
#             "first_name": user.first_name,
#             "last_name": user.last_name,
#         }
#     })


# # =========================
# # PROFILE
# # =========================
# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def user_profile(request):
#     user = request.user

#     return Response({
#         "id": user.id,
#         "username": user.username,
#         "email": user.email,
#         "first_name": user.first_name,
#         "last_name": user.last_name,
#     })


# # =========================
# # LOGOUT
# # =========================
# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def logout_user(request):
#     return Response({"message": "Logout successful"})


# # =========================
# # FORGOT PASSWORD (FIXED SAFE)
# # =========================
# @api_view(['POST'])
# def forgot_password(request):
#     email = request.data.get('email')

#     if not email:
#         return Response({"error": "Email required"}, status=400)

#     user = User.objects.filter(email=email).first()

#     if not user:
#         return Response({"error": "Email not found"}, status=404)

#     return Response({
#         "message": "User found",
#         "username": user.username
#     })


# # =========================
# # RESET PASSWORD (FIXED SAFE)
# # =========================
# @api_view(['POST'])
# def reset_password(request):
#     email = request.data.get('email')
#     new_password = request.data.get('new_password')

#     if not email or not new_password:
#         return Response({"error": "Required fields missing"}, status=400)

#     user = User.objects.filter(email=email).first()

#     if not user:
#         return Response({"error": "User not found"}, status=404)

#     user.set_password(new_password)
#     user.save()

#     return Response({"message": "Password reset successful"})


# # =========================
# # GOOGLE LOGIN (PLACEHOLDER)
# # =========================
# @api_view(['POST'])
# def google_login(request):
#     return Response({"message": "Google login not implemented yet"})


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



# import requests
# import uuid
# import random
# import string
# import time
# from datetime import datetime

# from django.conf import settings
# from rest_framework.decorators import api_view
# from rest_framework.response import Response


# def vtpass_headers():
#     print("API KEY:", settings.VTPASS_API_KEY)
#     print("SECRET KEY:", settings.VTPASS_SECRET_KEY)

#     return {
#         "Content-Type": "application/json",
#         "api-key": settings.VTPASS_API_KEY,
#         "secret-key": settings.VTPASS_SECRET_KEY,
#     }

# # =========================
# # REQUEST ID GENERATOR
# # =========================
# def generate_request_id():
#     now = datetime.now().strftime("%Y%m%d%H%M")
#     rand = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
#     return f"{now}{rand}"


# # =========================
# # SAFE REQUEST HELPER
# # =========================
# def vtpass_post(url, payload):
#     try:
#         res = requests.post(url, json=payload, headers=vtpass_headers(), timeout=30)

#         try:
#             return res.json(), res.status_code
#         except Exception:
#             return {"error": "Invalid VTpass response", "raw": res.text}, 500

#     except requests.exceptions.RequestException as e:
#         return {"error": "Network error", "details": str(e)}, 503


# # =========================
# # AIRTIME
# # =========================
# @api_view(['POST'])
# def buy_airtime(request):

#     service_map = {
#         "mtn": "mtn",
#         "airtel": "airtel",
#         "glo": "glo",
#         "9mobile": "9mobile"
#     }

#     network = request.data.get("network")
#     amount = request.data.get("amount")
#     phone = request.data.get("phone")

#     if not network or not amount or not phone:
#         return Response({"error": "network, amount, phone required"}, status=400)

#     service_id = service_map.get(network.lower())

#     if not service_id:
#         return Response({"error": "Invalid network"}, status=400)

#     payload = {
#         "request_id": str(uuid.uuid4()),
#         "serviceID": service_id,
#         "amount": amount,
#         "phone": phone
#     }

#     data, status = vtpass_post("https://sandbox.vtpass.com/api/pay", payload)
#     return Response(data, status=status)



# @api_view(['POST'])
# def buy_data(request):

#     network_map = {
#         "mtn": "mtn-data",
#         "airtel": "airtel-data",
#         "glo": "glo-data",
#         "9mobile": "etisalat-data"
#     }

#     network = request.data.get("network")
#     phone = request.data.get("phone")
#     variation_code = request.data.get("variation_code")
#     amount = request.data.get("amount")

#     if not network or not phone or not variation_code:
#         return Response({"error": "network, phone, variation_code required"}, status=400)

#     service_id = network_map.get(network.lower())

#     if not service_id:
#         return Response({"error": "Invalid network"}, status=400)

#     payload = {
#         "request_id": generate_request_id(),
#         "serviceID": service_id,
#         "billersCode": phone,
#         "variation_code": variation_code,
#         "amount": amount,
#         "phone": phone,
#     }

#     data, status = vtpass_post(
#         "https://sandbox.vtpass.com/api/pay",
#         payload
#     )

#     return Response(data, status=status)

# # =========================
# # GOTV
# # =========================
# import uuid
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# import requests


# def vtpass_get(url):
#     res = requests.get(url)
#     return res.json(), res.status_code

# import requests



# @api_view(['POST'])
# def buy_gotv(request):

#     billers_code = request.data.get("billersCode")
#     variation_code = request.data.get("variation_code")
#     phone = request.data.get("phone")
#     subscription_type = request.data.get("subscription_type", "change")

#     if not billers_code:
#         return Response({"error": "billersCode is required"}, status=400)

#     if not variation_code:
#         return Response({"error": "variation_code is required"}, status=400)

#     if not phone:
#         return Response({"error": "phone is required"}, status=400)

#     # 🔥 GET VARIATIONS
#     vtpass_variations, _ = vtpass_get(
#         "https://sandbox.vtpass.com/api/service-variations?serviceID=gotv"
#     )

#     real_price = None

#     for v in vtpass_variations["content"]["variations"]:
#         if v["variation_code"] == variation_code:
#             real_price = float(v["variation_amount"])

#     if real_price is None:
#         return Response({"error": "Invalid variation"}, status=400)

#     # 🔥 YOUR PROFIT (HIDDEN)
#     profit = 50
#     selling_price = real_price + profit

#     payload = {
#         "request_id": str(uuid.uuid4()),
#         "serviceID": "gotv",
#         "billersCode": billers_code,
#         "variation_code": variation_code,
#         "amount": real_price,  # VTpass only sees real price
#         "phone": phone,
#         "subscription_type": subscription_type,
#     }

#     data, http_status = vtpass_post(
#         "https://sandbox.vtpass.com/api/pay",
#         payload
#     )

#     # 🔥 STORE PROFIT (REAL WAY)
#     if data.get("code") == "000":
#         transaction = data["content"]["transactions"]

#         # ⚠️ THIS IS ONLY RESPONSE MODIFICATION
#         transaction["user_paid"] = selling_price
#         transaction["profit"] = profit

#         # 👉 BEST PRACTICE: SAVE TO DATABASE HERE
#         # Transaction.objects.create(...)

#     return Response(data, status=http_status)







# # =========================
# # STARTIMES
# # =========================
# import uuid
# import requests
# from rest_framework.decorators import api_view
# from rest_framework.response import Response


# import uuid
# import requests

# from rest_framework.decorators import api_view
# from rest_framework.response import Response

# import uuid
# import requests

# from django.conf import settings
# from rest_framework.decorators import api_view
# from rest_framework.response import Response


# @api_view(['POST'])
# def buy_startimes(request):

#     billers_code = request.data.get("billersCode")
#     variation_code = request.data.get("variation_code")
#     phone = request.data.get("phone")

#     # VALIDATION
#     if not billers_code:
#         return Response(
#             {"error": "billersCode is required"},
#             status=400
#         )

#     if not variation_code:
#         return Response(
#             {"error": "variation_code is required"},
#             status=400
#         )

#     if not phone:
#         return Response(
#             {"error": "phone is required"},
#             status=400
#         )

#     # GET STARTIMES VARIATIONS
#     try:
#         variation_response = requests.get(
#             "https://sandbox.vtpass.com/api/service-variations",
#             params={"serviceID": "startimes"},
#             headers={
#                 "api-key": settings.VTPASS_API_KEY,
#                 "public-key": settings.VTPASS_PUBLIC_KEY,
#             },
#             timeout=20,
#         )

#         data_variations = variation_response.json()

#     except Exception as e:
#         return Response({
#             "error": "Failed to fetch Startimes variations",
#             "details": str(e)
#         }, status=500)

#     # FIND REAL PRICE
#     real_price = None

#     for item in data_variations.get("content", {}).get("variations", []):
#         if item.get("variation_code") == variation_code:
#             real_price = float(item.get("variation_amount", 0))
#             break

#     if real_price is None:
#         return Response({
#             "error": "Invalid variation_code"
#         }, status=400)

#     # PROFIT
#     profit = 50
#     selling_price = real_price + profit

#     # PAYMENT PAYLOAD
#     payload = {
#         "request_id": str(uuid.uuid4()),
#         "serviceID": "startimes",
#         "billersCode": billers_code,
#         "variation_code": variation_code,
#         "amount": real_price,
#         "phone": phone,
#     }

#     try:
#         vtpass_response = requests.post(
#             "https://sandbox.vtpass.com/api/pay",
#             json=payload,
#             headers={
#                 "api-key": settings.VTPASS_API_KEY,
#                 "secret-key": settings.VTPASS_SECRET_KEY,
#                 "Content-Type": "application/json",
#                 "Accept": "application/json",
#             },
#             timeout=20,
#         )

#         data = vtpass_response.json()

#     except Exception as e:
#         return Response({
#             "error": "VTpass payment failed",
#             "details": str(e)
#         }, status=500)

#     # SUCCESS
#     if data.get("code") == "000":
#         transaction = data.get("content", {}).get("transactions", {})

#         transaction["user_paid"] = selling_price
#         transaction["profit"] = profit

#     return Response(
#         data,
#         status=vtpass_response.status_code
#     )
# # =========================
# # ELECTRICITY VERIFY
# # =========================
# @api_view(['POST'])
# def verify_meter(request):

#     payload = {
#         "billersCode": request.data.get("billersCode"),
#         "serviceID": request.data.get("serviceID"),
#         "type": request.data.get("type"),
#     }

#     try:
#         res = requests.post(
#             "https://vtpass.com/api/merchant-verify",
#             json=payload,
#             headers=vtpass_headers(),
#             timeout=30
#         )
#         return Response(res.json())
#     except Exception as e:
#         return Response({"error": str(e)}, status=503)






# # buy_showmax


# import uuid
# import requests

# from rest_framework.decorators import api_view
# from rest_framework.response import Response


# @api_view(['POST'])
# def buy_showmax(request):

#     billers_code = request.data.get("billersCode")
#     variation_code = request.data.get("variation_code")

#     if not billers_code:
#         return Response(
#             {"error": "billersCode is required"},
#             status=400,
#         )

#     if not variation_code:
#         return Response(
#             {"error": "variation_code is required"},
#             status=400,
#         )

#     # ==========================
#     # GET SHOWMAX VARIATIONS
#     # ==========================
#     try:
#         res = requests.get(
#             "https://sandbox.vtpass.com/api/service-variations",
#             params={"serviceID": "showmax"},
#             timeout=20,
#         )

#         data_variations = res.json()

#     except Exception as e:
#         return Response({
#             "error": "Failed to fetch Showmax plans",
#             "details": str(e)
#         }, status=500)

#     # ==========================
#     # FIND REAL PRICE
#     # ==========================
#     real_price = None

#     for v in data_variations.get("content", {}).get("variations", []):
#         if v.get("variation_code") == variation_code:
#             real_price = float(v.get("variation_amount", 0))
#             break

#     if real_price is None:
#         return Response({
#             "error": "Invalid variation_code"
#         }, status=400)

#     # ==========================
#     # YOUR PROFIT
#     # ==========================
#     profit = 50
#     selling_price = real_price + profit

#     # ==========================
#     # PAYMENT PAYLOAD
#     # ==========================
#     payload = {
#         "request_id": str(uuid.uuid4()),
#         "serviceID": "showmax",
#         "billersCode": billers_code,
#         "variation_code": variation_code,
#         "amount": real_price,
#     }

#     try:
#         vtpass_response = requests.post(
#             "https://sandbox.vtpass.com/api/pay",
#             json=payload,
#             timeout=20,
#             headers={
#                 "Content-Type": "application/json",
#                 "Accept": "application/json",
#             }
#         )

#         data = vtpass_response.json()

#     except Exception as e:
#         return Response({
#             "error": "VTpass payment failed",
#             "details": str(e)
#         }, status=500)

#     # ==========================
#     # SUCCESS
#     # ==========================
#     if data.get("code") == "000":
#         transaction = data.get("content", {}).get("transactions", {})

#         transaction["user_paid"] = selling_price
#         transaction["profit"] = profit

#     return Response(
#         data,
#         status=vtpass_response.status_code,
#     )


# # =========================
# # ELECTRICITY BUY
# # =========================
# @api_view(['POST'])
# def buy_electricity(request):

#     payload = {
#         "request_id": str(int(time.time())),
#         "serviceID": request.data.get("service_id"),
#         "billersCode": request.data.get("meter_number"),
#         "variation_code": request.data.get("meter_type"),
#         "amount": request.data.get("amount"),
#         "phone": request.data.get("phone")
#     }

#     data, status = vtpass_post("https://vtpass.com/api/pay", payload)
#     return Response(data, status=status)






# # Education



# # waec_variations



# @api_view(['GET'])
# def waec_variations(request):
#     res = requests.get(
#         "https://sandbox.vtpass.com/api/service-variations?serviceID=waec-registration",
#         headers=vtpass_headers()
#     )
#     return Response(res.json())



# # buy_waec_registration


# @api_view(['POST'])
# def buy_waec_registration(request):

#     payload = {
#         "request_id": generate_request_id(),
#         "serviceID": "waec-registration",
#         "variation_code": request.data.get("variation_code"),
#         "quantity": request.data.get("quantity", 1),
#         "phone": request.data.get("phone"),
#     }

#     data, status_code = vtpass_post(
#         "https://sandbox.vtpass.com/api/pay",
#         payload
#     )

#     return Response(data, status=status_code)



# # requery_transaction

# @api_view(['POST'])
# def requery_transaction(request):

#     payload = {
#         "request_id": request.data.get("request_id")
#     }

#     data, status_code = vtpass_post(
#         "https://sandbox.vtpass.com/api/requery",
#         payload
#     )

#     return Response(data, status=status_code)

# # result checker


# @api_view(['GET'])
# def waec_result_variations(request):
#     url = "https://sandbox.vtpass.com/api/service-variations?serviceID=waec"
#     res = requests.get(url, headers=vtpass_headers())
#     return Response(res.json())




# @api_view(['POST'])
# def buy_waec_result_pin(request):

#     payload = {
#         "request_id": generate_request_id(),
#         "serviceID": "waec",
#         "variation_code": request.data.get("variation_code"),
#         "quantity": request.data.get("quantity", 1),
#         "phone": request.data.get("phone"),
#     }

#     data, status = vtpass_post(
#         "https://sandbox.vtpass.com/api/pay",
#         payload
#     )

#     return Response(data, status=status)




# @api_view(['POST'])
# def waec_result_requery(request):

#     payload = {
#         "request_id": request.data.get("request_id")
#     }

#     data, status = vtpass_post(
#         "https://sandbox.vtpass.com/api/requery",
#         payload
#     )

#     return Response(data, status=status)




#     # Jamb
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# import requests

# # make sure these exist in your project
# # from .utils import vtpass_headers, vtpass_post, generate_request_id


# # =========================
# # JAMB VARIATIONS (GET)
# # =========================
# @api_view(['GET'])
# def jamb_variations(request):
#     url = "https://sandbox.vtpass.com/api/service-variations?serviceID=jamb"
#     res = requests.get(url, headers=vtpass_headers())
#     return Response(res.json())


# # =========================
# # VERIFY / REQUERY (POST)
# # =========================
# @api_view(['POST'])
# def jamb_requery(request):

#     payload = {
#         "request_id": request.data.get("request_id")
#     }

#     data, status = vtpass_post(
#         "https://sandbox.vtpass.com/api/requery",
#         payload
#     )

#     return Response(data, status=status)


# # =========================
# # BUY JAMB PIN (POST)
# # =========================
# @api_view(['POST'])
# def buy_jamb_pin(request):

#     payload = {
#         "request_id": generate_request_id(),
#         "serviceID": "jamb",
#         "variation_code": request.data.get("variation_code"),
#         "billersCode": request.data.get("billersCode", "0123456789"),
#         "phone": request.data.get("phone")
#     }

#     data, status = vtpass_post(
#         "https://sandbox.vtpass.com/api/pay",
#         payload
#     )

#     return Response(data, status=status)





# import base64

# def vtpass_auth():
#     credentials = f"{settings.VTPASS_EMAIL}:{settings.VTPASS_PASSWORD}"
#     token = base64.b64encode(credentials.encode()).decode()

#     return {
#         "Authorization": f"Basic {token}",
#         "Content-Type": "application/json"
#     }






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

#     PROFIT = 100  # backend-only

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


# # buy_gotv






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

# @api_view(['POST'])
# def register_user(request):
#     username = request.data.get('username')
#     email = request.data.get('email')
#     first_name = request.data.get('first_name')
#     last_name = request.data.get('last_name')
#     password = request.data.get('password')

#     if not username or not password:
#         return Response({"error": "Username and password required"}, status=400)

#     if User.objects.filter(username=username).exists():
#         return Response({"error": "Username exists"}, status=400)

#     if email and User.objects.filter(email=email).exists():
#         return Response({"error": "Email exists"}, status=400)

#     user = User.objects.create_user(
#         username=username,
#         email=email,
#         password=password,
#         first_name=first_name,
#         last_name=last_name
#     )

#     # 🔥 GENERATE TOKEN (THIS FIXES YOUR 401 ISSUE)
#     refresh = RefreshToken.for_user(user)

#     return Response({
#         "message": "User created",
#         "user": {
#             "id": user.id,
#             "username": user.username,
#             "first_name": user.first_name,
#             "last_name": user.last_name,
#         },
#         "token": str(refresh.access_token)   # ✅ IMPORTANT
#     }, status=201)



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








# =========================
# LOGIN (JWT)
# =========================
# @api_view(['POST'])
# def login_user(request):
#     username = request.data.get("username")
#     password = request.data.get("password")

#     user = authenticate(username=username, password=password)

#     if user is None:
#         return Response({"error": "Invalid credentials"}, status=400)

#     token = RefreshToken.for_user(user)

#     return Response({
#         "access": str(token.access_token),
#         "refresh": str(token),
#         "user": {
#             "id": user.id,
#             "username": user.username,
#             "first_name": user.first_name,
#             "last_name": user.last_name,
#         }
#     })

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

    if not username or not password:
        return Response(
            {"error": "Username and password required"},
            status=400
        )

    user = authenticate(
        username=username,
        password=password
    )

    if user is None:
        return Response(
            {"error": "Invalid credentials"},
            status=400
        )

    token = RefreshToken.for_user(user)

    return Response({
        "access": str(token.access_token),
        "refresh": str(token),
        "user": {
            "id": user.id,
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
        }
    })
# @api_view(['POST'])
# def login_user(request):
#     username = request.data.get("username")
#     password = request.data.get("password")

#     user = authenticate(username=username, password=password)

#     if user is None:
#         return Response({"error": "Invalid credentials"}, status=400)

#     # Send security alert email
#     if user.email:
#         try:
#             send_mail(
#                 subject="Security Alert - New Login",
#                 message=f"""
# Hello {user.first_name or user.username},

# We detected a login to your Mass Data account.

# If this was you, you can ignore this email.

# If this was NOT you, please change your password immediately.

# Mass Data Security Team
# """,
#                 from_email=settings.DEFAULT_FROM_EMAIL,
#                 recipient_list=[user.email],
#                 fail_silently=False,
#             )
#         except Exception as e:
#             print("Email Error:", e)

#     # Generate JWT token
#     token = RefreshToken.for_user(user)

#     return Response({
#         "access": str(token.access_token),
#         "refresh": str(token),
#         "user": {
#             "id": user.id,
#             "username": user.username,
#             "first_name": user.first_name,
#             "last_name": user.last_name,
#         }
#     })
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






@api_view(['GET'])
def service_variations(request):
    service_id = request.GET.get("serviceID")

    if not service_id:
        return Response({"error": "serviceID is required"}, status=400)

    headers = {
        "api-key": settings.VTPASS_API_KEY,
        "public-key": settings.VTPASS_PUBLIC_KEY,
    }

    response = requests.get(
        "https://sandbox.vtpass.com/api/service-variations",
        params={"serviceID": service_id},
        headers=headers
    )

    data = response.json()

    variations = data.get("content", {}).get("variations", [])

    PROFIT = 1  # backend-only

    clean = []

    for item in variations:
        try:
            base = float(item.get("variation_amount", 0))
        except:
            base = 0

        clean.append({
            "variation_code": item.get("variation_code"),
            "name": item.get("name"),
            "price": base + PROFIT   # ONLY final price shown
        })

    return Response({
        "response_description": data.get("response_description"),
        "content": {
            "serviceID": service_id,
            "variations": clean
        }
    })




# webbook
