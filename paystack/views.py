# from decimal import Decimal
# import requests

# from django.conf import settings
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response

# from .models import Wallet, Transaction


# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def verify_payment(request):

#     reference = request.data.get("reference")

#     if not reference:
#         return Response(
#             {"error": "Reference required"},
#             status=400
#         )

#     # Already processed?
#     existing = Transaction.objects.filter(
#         reference=reference
#     ).first()

#     if existing:
#         wallet, _ = Wallet.objects.get_or_create(
#             owner=request.user,
#             defaults={"amount": Decimal("0.00")}
#         )

#         return Response({
#             "status": "success",
#             "amount": str(existing.amount),
#             "new_balance": str(wallet.amount),
#             "message": "Already processed"
#         })

#     url = f"https://api.paystack.co/transaction/verify/{reference}"

#     headers = {
#         "Authorization":
#         f"Bearer {settings.PAYSTACK_SECRET_KEY}"
#     }

#     response = requests.get(
#         url,
#         headers=headers
#     )

#     data = response.json()

#     print("PAYSTACK RESPONSE:", data)

#     if not data.get("status"):
#         return Response(
#             {"error": "Verification failed"},
#             status=400
#         )

#     payment = data["data"]

#     if payment["status"] != "success":
#         return Response(
#             {"error": "Payment not successful"},
#             status=400
#         )

#     amount = Decimal(
#         str(payment["amount"])
#     ) / Decimal("100")

#     user = request.user

#     print("USER ID:", user.id)
#     print("USERNAME:", user.username)

#     wallet, created = Wallet.objects.get_or_create(
#         owner=user,
#         defaults={"amount": Decimal("0.00")}
#     )

#     print("WALLET ID:", wallet.id)
#     print("OLD BALANCE:", wallet.amount)

#     wallet.amount += amount
#     wallet.save(update_fields=["amount"])

#     wallet.refresh_from_db()

#     print("NEW BALANCE:", wallet.amount)

#     Transaction.objects.create(
#         user=user,
#         reference=reference,
#         amount=amount,
#         status="success",
#         email=payment["customer"]["email"]
#     )

#     return Response({
#         "status": "success",
#         "amount": str(amount),
#         "new_balance": str(wallet.amount),
#         "message": "Wallet funded successfully"
#     })

# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def wallet_balance(request):

#     wallet, _ = Wallet.objects.get_or_create(
#         owner=request.user,
#         defaults={"amount": Decimal("0.00")}
#     )

#     return Response({
#         "username": request.user.username,
#         "balance": str(wallet.amount)
#     })


    



# from decimal import Decimal
# import requests

# from django.conf import settings
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response

# from .models import Wallet, Transaction


# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def verify_payment(request):

#     reference = request.data.get("reference")

#     if not reference:
#         return Response(
#             {"error": "Reference required"},
#             status=400
#         )

#     # Already processed?
#     existing = Transaction.objects.filter(
#         reference=reference
#     ).first()

#     if existing:
#         wallet, _ = Wallet.objects.get_or_create(
#             owner=request.user,
#             defaults={"amount": Decimal("0.00")}
#         )

#         return Response({
#             "status": "success",
#             "amount": str(existing.amount),
#             "new_balance": str(wallet.amount),
#             "message": "Already processed"
#         })

#     url = f"https://api.paystack.co/transaction/verify/{reference}"

#     headers = {
#         "Authorization":
#         f"Bearer {settings.PAYSTACK_SECRET_KEY}"
#     }

#     response = requests.get(
#         url,
#         headers=headers
#     )

#     data = response.json()

#     print("PAYSTACK RESPONSE:", data)

#     if not data.get("status"):
#         return Response(
#             {"error": "Verification failed"},
#             status=400
#         )

#     payment = data["data"]

#     if payment["status"] != "success":
#         return Response(
#             {"error": "Payment not successful"},
#             status=400
#         )

#     amount = Decimal(
#         str(payment["amount"])
#     ) / Decimal("100")

#     user = request.user

#     print("USER ID:", user.id)
#     print("USERNAME:", user.username)

#     wallet, created = Wallet.objects.get_or_create(
#         owner=user,
#         defaults={"amount": Decimal("0.00")}
#     )

#     print("WALLET ID:", wallet.id)
#     print("OLD BALANCE:", wallet.amount)

#     wallet.amount += amount
#     wallet.save(update_fields=["amount"])

#     wallet.refresh_from_db()

#     print("NEW BALANCE:", wallet.amount)

#     Transaction.objects.create(
#         user=user,
#         reference=reference,
#         amount=amount,
#         status="success",
#         email=payment["customer"]["email"]
#     )

#     return Response({
#         "status": "success",
#         "amount": str(amount),
#         "new_balance": str(wallet.amount),
#         "message": "Wallet funded successfully"
#     })

# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def wallet_balance(request):

#     wallet, _ = Wallet.objects.get_or_create(
#         owner=request.user,
#         defaults={"amount": Decimal("0.00")}
#     )

#     return Response({
#         "username": request.user.username,
#         "balance": str(wallet.amount)
#     })


    




from decimal import Decimal
import requests

from django.conf import settings
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Wallet, Transaction


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def verify_payment(request):

    reference = request.data.get("reference")

    if not reference:
        return Response(
            {"error": "Reference required"},
            status=400
        )

    # Already processed?
    existing = Transaction.objects.filter(
        reference=reference
    ).first()

    if existing:
        wallet, _ = Wallet.objects.get_or_create(
            owner=request.user,
            defaults={"amount": Decimal("0.00")}
        )

        return Response({
            "status": "success",
            "amount": str(existing.amount),
            "new_balance": str(wallet.amount),
            "message": "Already processed"
        })

    url = f"https://api.paystack.co/transaction/verify/{reference}"

    headers = {
        "Authorization":
        f"Bearer {settings.PAYSTACK_SECRET_KEY}"
    }

    response = requests.get(
        url,
        headers=headers
    )

    data = response.json()

    print("PAYSTACK RESPONSE:", data)

    if not data.get("status"):
        return Response(
            {"error": "Verification failed"},
            status=400
        )

    payment = data["data"]

    if payment["status"] != "success":
        return Response(
            {"error": "Payment not successful"},
            status=400
        )

    amount = Decimal(
        str(payment["amount"])
    ) / Decimal("100")

    user = request.user

    print("USER ID:", user.id)
    print("USERNAME:", user.username)

    wallet, created = Wallet.objects.get_or_create(
        owner=user,
        defaults={"amount": Decimal("0.00")}
    )

    print("WALLET ID:", wallet.id)
    print("OLD BALANCE:", wallet.amount)

    wallet.amount += amount
    wallet.save(update_fields=["amount"])

    wallet.refresh_from_db()

    print("NEW BALANCE:", wallet.amount)

    # Transaction.objects.create(
    #     user=user,
    #     reference=reference,
    #     amount=amount,
    #     status="success",
    #     email=payment["customer"]["email"]
    # )
    Transaction.objects.create(
    user=user,
    request_id=reference,
    amount=amount,
    status="success",
    email=payment["customer"]["email"]
)
    return Response({
        "status": "success",
        "amount": str(amount),
        "new_balance": str(wallet.amount),
        "message": "Wallet funded successfully"
    })

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def wallet_balance(request):

    wallet, _ = Wallet.objects.get_or_create(
        owner=request.user,
        defaults={"amount": Decimal("0.00")}
    )

    return Response({
        "username": request.user.username,
        "balance": str(wallet.amount)
    })





# from decimal import Decimal
# from django.db import transaction
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response

# from .models import Wallet


# @api_view(["POST"])
# @permission_classes([IsAuthenticated])
# def buy_product(request):

#     user = request.user

#     product = request.data.get("product")
#     amount = request.data.get("amount")

#     if not product:
#         return Response({"error": "Product is required."}, status=400)

#     try:
#         amount = Decimal(str(amount))
#     except Exception:
#         return Response({"error": "Invalid amount."}, status=400)

#     with transaction.atomic():

#         wallet, _ = Wallet.objects.select_for_update().get_or_create(
#             owner=user,
#             defaults={"amount": Decimal("0.00")}
#         )

#         # Check balance first
#         if wallet.amount < amount:
#             return Response({
#                 "success": False,
#                 "message": "Insufficient balance.",
#                 "wallet_balance": str(wallet.amount),
#             }, status=400)

#         product = product.lower()

#         if product == "data":

#             phone = request.data.get("phone")
#             network = request.data.get("network")
#             variation_code = request.data.get("variation_code")

#             if not phone:
#                 return Response({"error": "Phone number is required."}, status=400)

#             if not network:
#                 return Response({"error": "Network is required."}, status=400)

#             if not variation_code:
#                 return Response({"error": "Variation code is required."}, status=400)

#             # TODO:
#             # Call VTpass here

#             wallet.amount -= amount
#             wallet.save()

#             return Response({
#                 "success": True,
#                 "message": "Data purchase successful.",
#                 "phone": phone,
#                 "network": network,
#                 "variation_code": variation_code,
#                 "amount": str(amount),
#                 "new_balance": str(wallet.amount),
#             })

# #


# from decimal import Decimal
# from django.db import transaction
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response

# from .models import Wallet


# @api_view(["POST"])
# @permission_classes([IsAuthenticated])
# def buy_product(request):

#     user = request.user

#     product = request.data.get("product")
#     amount = request.data.get("amount")

#     if not product:
#         return Response({"error": "Product is required."}, status=400)

#     try:
#         amount = Decimal(str(amount))
#     except Exception:
#         return Response({"error": "Invalid amount."}, status=400)

#     product = product.lower()

#     with transaction.atomic():

#         wallet, _ = Wallet.objects.select_for_update().get_or_create(
#             owner=user,
#             defaults={"amount": Decimal("0.00")}
#         )

#         # ❌ WALLET CHECK (ALWAYS FIRST)
#         if wallet.amount < amount:
#             return Response({
#                 "success": False,
#                 "message": "Insufficient balance.",
#                 "wallet_balance": str(wallet.amount),
#             }, status=400)

#         # =========================
#         # 📦 DATA PURCHASE
#         # =========================
#         if product == "data":

#             phone = request.data.get("phone")
#             network = request.data.get("network")
#             variation_code = request.data.get("variation_code")

#             if not phone or not network or not variation_code:
#                 return Response({
#                     "error": "Phone, network and variation_code are required."
#                 }, status=400)

#             # TODO: CALL VTpass HERE

#             wallet.amount -= amount
#             wallet.save()

#             return Response({
#                 "success": True,
#                 "message": "Data purchase successful.",
#                 "product": "data",
#                 "phone": phone,
#                 "network": network,
#                 "variation_code": variation_code,
#                 "amount": str(amount),
#                 "new_balance": str(wallet.amount),
#             })

#         # =========================
#         # 📞 AIRTIME PURCHASE
#         # =========================
#         elif product == "airtime":

#             phone = request.data.get("phone")
#             network = request.data.get("network")

#             if not phone or not network:
#                 return Response({
#                     "error": "Phone and network are required."
#                 }, status=400)

#             # TODO: CALL VTpass HERE

#             wallet.amount -= amount
#             wallet.save()

#             return Response({
#                 "success": True,
#                 "message": "Airtime purchase successful.",
#                 "product": "airtime",
#                 "phone": phone,
#                 "network": network,
#                 "amount": str(amount),
#                 "new_balance": str(wallet.amount),
#             })

#         # =========================
#         # ❌ INVALID PRODUCT
#         # =========================
#         return Response({
#             "error": "Invalid product. Use 'data' or 'airtime'."
#         }, status=400)



# from decimal import Decimal
# from django.db import transaction
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response

# from .models import Wallet


# @api_view(["POST"])
# @permission_classes([IsAuthenticated])
# def buy_product(request):

#     user = request.user

#     product = request.data.get("product")
#     amount = request.data.get("amount")

#     # ❌ Validate product
#     if not product:
#         return Response({"error": "Product is required."}, status=400)

#     product = str(product).lower().strip()

#     # ❌ Validate amount safely
#     try:
#         amount = Decimal(str(amount))
#     except:
#         return Response({"error": "Invalid amount."}, status=400)

#     if amount <= 0:
#         return Response({"error": "Amount must be greater than 0."}, status=400)

#     with transaction.atomic():

#         wallet = Wallet.objects.select_for_update().get_or_create(
#             owner=user,
#             defaults={"amount": Decimal("0.00")}
#         )[0]

#         # ❌ Wallet check (FIRST RULE)
#         if wallet.amount < amount:
#             return Response({
#                 "success": False,
#                 "message": "Insufficient balance.",
#                 "wallet_balance": str(wallet.amount),
#             }, status=400)

#         # =========================
#         # 📦 DATA PURCHASE
#         # =========================
#         if product == "data":

#             phone = request.data.get("phone")
#             network = request.data.get("network")
#             variation_code = request.data.get("variation_code")

#             if not all([phone, network, variation_code]):
#                 return Response({
#                     "error": "phone, network, variation_code required"
#                 }, status=400)

#             # TODO: VTU API CALL HERE

#             wallet.amount -= amount
#             wallet.save()

#             return Response({
#                 "success": True,
#                 "message": "Data purchase successful",
#                 "product": "data",
#                 "phone": phone,
#                 "network": network,
#                 "variation_code": variation_code,
#                 "amount": str(amount),
#                 "new_balance": str(wallet.amount),
#             })

#         # =========================
#         # 📞 AIRTIME PURCHASE
#         # =========================
#         elif product == "airtime":

#             phone = request.data.get("phone")
#             network = request.data.get("network")

#             if not phone or not network:
#                 return Response({
#                     "error": "phone and network required"
#                 }, status=400)

#             # TODO: VTU API CALL HERE

#             wallet.amount -= amount
#             wallet.save()

#             return Response({
#                 "success": True,
#                 "message": "Airtime purchase successful",
#                 "product": "airtime",
#                 "phone": phone,
#                 "network": network,
#                 "amount": str(amount),
#                 "new_balance": str(wallet.amount),
#             })

#         # ❌ INVALID PRODUCT
#         return Response({
#             "error": "Invalid product. Use 'data' or 'airtime'."
#         }, status=400)



# from decimal import Decimal
# from django.db import transaction
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response

# from .models import Wallet


# @api_view(["POST"])
# @permission_classes([IsAuthenticated])
# def buy_product(request):

#     user = request.user

#     product = request.data.get("product")
#     amount = request.data.get("amount")

#     if not product:
#         return Response({"error": "Product is required."}, status=400)

#     product = str(product).lower().strip()

#     try:
#         amount = Decimal(str(amount))
#     except Exception:
#         return Response({"error": "Invalid amount."}, status=400)

#     if amount <= 0:
#         return Response({"error": "Amount must be greater than 0."}, status=400)

#     with transaction.atomic():

#         wallet, _ = Wallet.objects.select_for_update().get_or_create(
#             owner=user,
#             defaults={"amount": Decimal("0.00")}
#         )

#         if wallet.amount < amount:
#             return Response({
#                 "success": False,
#                 "message": "Insufficient balance.",
#                 "wallet_balance": str(wallet.amount),
#             }, status=400)

#         # =========================
#         # DATA PURCHASE
#         # =========================
#         if product == "data":

#             phone = request.data.get("phone")
#             network = request.data.get("network")
#             variation_code = request.data.get("variation_code")

#             if not all([phone, network, variation_code]):
#                 return Response({
#                     "error": "phone, network and variation_code are required."
#                 }, status=400)

#             # TODO: Call your VTU API here

#             wallet.amount -= amount
#             wallet.save(update_fields=["amount"])

#             return Response({
#                 "success": True,
#                 "message": "Data purchase successful.",
#                 "product": "data",
#                 "phone": phone,
#                 "network": network,
#                 "variation_code": variation_code,
#                 "amount": str(amount),
#                 "new_balance": str(wallet.amount),
#             })

#         # =========================
#         # AIRTIME PURCHASE
#         # =========================
#         elif product == "airtime":
#              network = request.data.get("network")
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

            # phone = request.data.get("phone")
            # network = request.data.get("network")

            # if not phone or not network:
            #     return Response({
            #         "error": "phone and network are required."
            #     }, status=400)

            # # TODO: Call your VTU API here

            # wallet.amount -= amount
            # wallet.save(update_fields=["amount"])

            # return Response({
            #     "success": True,
            #     "message": "Airtime purchase successful.",
            #     "product": "airtime",
            #     "phone": phone,
            #     "network": network,
            #     "amount": str(amount),
            #     "new_balance": str(wallet.amount),
            # })

        # =========================
        # CABLE TV SUBSCRIPTION
        # =========================
        # elif product == "cabletv":

        #     service_id = request.data.get("serviceID")
        #     variation_code = request.data.get("variation_code")
        #     smartcard_number = request.data.get("smartcard_number")

        #     if not all([service_id, variation_code, smartcard_number]):
        #         return Response({
        #             "error": "serviceID, variation_code and smartcard_number are required."
        #         }, status=400)

        #     # TODO: Call your Cable TV API here

        #     wallet.amount -= amount
        #     wallet.save(update_fields=["amount"])

        #     return Response({
        #         "success": True,
        #         "message": "Cable TV subscription successful.",
        #         "product": "cabletv",
        #         "serviceID": service_id,
        #         "variation_code": variation_code,
        #         "smartcard_number": smartcard_number,
        #         "amount": str(amount),
        #         "new_balance": str(wallet.amount),
        #     })

        # return Response({
        #     "error": "Invalid product. Use 'airtime', 'data' or 'cabletv'."
        # }, status=400)


import uuid
import time
import random
import string
import base64
from decimal import Decimal
from datetime import datetime

import requests
from django.conf import settings
from django.db import transaction

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Wallet


# =========================
# VT PASS CORE (ONE SYSTEM)
# =========================

def vtpass_headers():
    return {
        "api-key": settings.VTPASS_API_KEY,
        "secret-key": settings.VTPASS_SECRET_KEY,
        "Content-Type": "application/json",
    }


def generate_request_id():
    return f"{datetime.now().strftime('%Y%m%d%H%M%S')}-{uuid.uuid4().hex[:6]}"


def vtpass_post(url, payload):
    try:
        res = requests.post(
            url,
            json=payload,
            headers=vtpass_headers(),
            timeout=30
        )
        return res.json(), res.status_code
    except Exception as e:
        return {"error": "network error", "details": str(e)}, 503


def vtpass_get(url, params=None):
    try:
        res = requests.get(url, params=params, headers=vtpass_headers(), timeout=30)
        return res.json(), res.status_code
    except Exception as e:
        return {"error": "network error", "details": str(e)}, 503


# =========================
# WALLET BUY SYSTEM
# =========================

# @api_view(["POST"])
# @permission_classes([IsAuthenticated])
# def buy_product(request):

#     user = request.user
#     product = str(request.data.get("product", "")).lower().strip()

#     try:
#         amount = Decimal(str(request.data.get("amount")))
#     except:
#         return Response({"error": "Invalid amount"}, status=400)

#     if amount <= 0:
#         return Response({"error": "Amount must be > 0"}, status=400)

#     with transaction.atomic():

#         wallet, _ = Wallet.objects.select_for_update().get_or_create(
#             owner=user,
#             defaults={"amount": Decimal("0.00")}
#         )

#         if wallet.amount < amount:
#             return Response({"error": "Insufficient balance"}, status=400)

#         payload = None

#         # =========================
#         # AIRTIME
#         # =========================
#         if product == "airtime":
#             payload = {
#                 "request_id": generate_request_id(),
#                 "serviceID": request.data.get("network"),
#                 "amount": str(amount),
#                 "phone": request.data.get("phone")
#             }

#         # =========================
#         # DATA
#         # =========================
#         elif product == "data":
#             payload = {
#                 "request_id": generate_request_id(),
#                 "serviceID": request.data.get("network"),
#                 "billersCode": request.data.get("phone"),
#                 "variation_code": request.data.get("variation_code"),
#                 "amount": str(amount),
#                 "phone": request.data.get("phone")
#             }

#         # =========================
#         # CABLE TV
#         # =========================
#         elif product == "cabletv":
#             payload = {
#                 "request_id": generate_request_id(),
#                 "serviceID": request.data.get("serviceID"),
#                 "billersCode": request.data.get("smartcard_number"),
#                 "variation_code": request.data.get("variation_code"),
#                 "amount": str(amount),
#                 "phone": request.data.get("phone")
#             }

#         else:
#             return Response({"error": "Invalid product"}, status=400)

#         # =========================
#         # CALL VTU ONCE
#         # =========================
#         data, status = vtpass_post(
#             "https://sandbox.vtpass.com/api/pay",
#             payload
#         )

#         if status != 200:
#             return Response(data, status=status)

#         wallet.amount -= amount
#         wallet.save(update_fields=["amount"])

#         return Response({
#             "success": True,
#             "product": product,
#             "amount": str(amount),
#             "new_balance": str(wallet.amount),
#             "api_response": data
#         })


# # =========================
# # AIRTIME (STANDALONE)
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

#     if not all([network, amount, phone]):
#         return Response({"error": "missing fields"}, status=400)

#     payload = {
#         "request_id": generate_request_id(),
#         "serviceID": service_map.get(network.lower()),
#         "amount": amount,
#         "phone": phone
#     }

#     data, status = vtpass_post(
#         "https://sandbox.vtpass.com/api/pay",
#         payload
#     )

#     return Response(data, status=status)


# # =========================
# # DATA (STANDALONE)
# # =========================

# @api_view(['POST'])
# def buy_data(request):

#     network_map = {
#         "mtn": "mtn-data",
#         "airtel": "airtel-data",
#         "glo": "glo-data",
#         "9mobile": "etisalat-data"
#     }

#     payload = {
#         "request_id": generate_request_id(),
#         "serviceID": network_map.get(request.data.get("network", "").lower()),
#         "billersCode": request.data.get("phone"),
#         "variation_code": request.data.get("variation_code"),
#         "amount": request.data.get("amount"),
#         "phone": request.data.get("phone"),
#     }

#     data, status = vtpass_post(
#         "https://sandbox.vtpass.com/api/pay",
#         payload
#     )

#     return Response(data, status=status)


# # =========================
# # GOTV / STARTIMES / SHOWMAX (CLEAN PATTERN)
# # =========================

# def get_variation(service_id):
#     return vtpass_get(
#         "https://sandbox.vtpass.com/api/service-variations",
#         params={"serviceID": service_id}
#     )


# @api_view(['POST'])
# def buy_gotv(request):

#     billers_code = request.data.get("billersCode")
#     variation_code = request.data.get("variation_code")
#     phone = request.data.get("phone")

#     if not all([billers_code, variation_code, phone]):
#         return Response({"error": "missing fields"}, status=400)

#     variations, _ = get_variation("gotv")

#     real_price = next(
#         (float(v["variation_amount"]) for v in variations["content"]["variations"]
#          if v["variation_code"] == variation_code),
#         None
#     )

#     if real_price is None:
#         return Response({"error": "invalid variation"}, status=400)

#     payload = {
#         "request_id": generate_request_id(),
#         "serviceID": "gotv",
#         "billersCode": billers_code,
#         "variation_code": variation_code,
#         "amount": real_price,
#         "phone": phone,
#     }

#     data, status = vtpass_post("https://sandbox.vtpass.com/api/pay", payload)
#     return Response(data, status=status)


# from decimal import Decimal
# from django.db import transaction
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response

# # ======================================================
# # 🔥 VTU SERVICE MAPPING (REAL VTpass FORMAT)
# # ======================================================

# VTU_SERVICE_MAP = {
#     # AIRTIME
#     "mtn": "mtn",
#     "airtel": "airtel",
#     "glo": "glo",
#     "9mobile": "etisalat",
#     "intl": "intl",

#     # DATA (VTpass expects base service only)
#     "mtn-data": "mtn",
#     "airtel-data": "airtel",
#     "glo-data": "glo",
#     "glo-sme": "glo-sme-data",
#     "9mobile-data": "etisalat",
#     "smile": "smile-direct",
#     "spectranet": "spectranet",
# }


# @api_view(["POST"])
# @permission_classes([IsAuthenticated])
# def buy_product(request):

#     user = request.user
#     product = str(request.data.get("product", "")).lower().strip()
#     network = request.data.get("network")

#     serviceID = VTU_SERVICE_MAP.get(network)

#     if not serviceID:
#         return Response({"error": "Invalid network"}, status=400)

#     try:
#         amount = Decimal(str(request.data.get("amount")))
#     except Exception:
#         return Response({"error": "Invalid amount"}, status=400)

#     if amount <= 0:
#         return Response({"error": "Amount must be greater than zero"}, status=400)

#     phone = request.data.get("phone")
#     if not phone:
#         return Response({"error": "Phone is required"}, status=400)

#     with transaction.atomic():

#         wallet, _ = Wallet.objects.select_for_update().get_or_create(
#             owner=user,
#             defaults={"amount": Decimal("0.00")}
#         )

#         if wallet.amount < amount:
#             return Response({"error": "Insufficient balance"}, status=400)

#         request_id = generate_request_id()

#         payload = {
#             "request_id": request_id,
#             "amount": str(amount),
#             "phone": phone,
#         }

#         # ======================================================
#         # 🔥 AIRTIME (ALL NETWORKS)
#         # ======================================================
#         if product == "airtime":

#             payload.update({
#                 "serviceID": serviceID,
#             })

#         # ======================================================
#         # 🔥 DATA (ALL PLANS VIA VARIATION CODE)
#         # ======================================================
#         elif product == "data":

#             variation_code = request.data.get("variation_code")

#             if not variation_code:
#                 return Response({"error": "variation_code required"}, status=400)

#             payload.update({
#                 "serviceID": serviceID,
#                 "billersCode": phone,
#                 "variation_code": variation_code,
#             })

#         else:
#             return Response({"error": "Invalid product type"}, status=400)

#         # ======================================================
#         # 🔥 CALL VTpass
#         # ======================================================
#         data, status_code = vtpass_post(
#             "https://sandbox.vtpass.com/api/pay",
#             payload
#         )

#         if status_code != 200:
#             return Response(data, status=status_code)

#         # ======================================================
#         # SAVE TRANSACTION
#         # ======================================================
#         Transaction.objects.create(
#             user=user,
#             request_id=request_id,
#             transaction_id="",
#             product_name=product,
#             phone=phone,
#             amount=amount,
#             total_amount=amount,
#             status="pending",
#         )

#         # ======================================================
#         # DEBIT WALLET
#         # ======================================================
#         wallet.amount -= amount
#         wallet.save(update_fields=["amount"])

#         return Response({
#             "success": True,
#             "message": "Transaction sent to VTpass successfully",
#             "request_id": request_id,
#             "product": product,
#             "serviceID": serviceID,
#             "amount": str(amount),
#             "new_balance": str(wallet.amount),
#             "api_response": data,
#         })


# @api_view(["POST"])
# @permission_classes([IsAuthenticated])
# def buy_product(request):

#     user = request.user
#     product = str(request.data.get("product", "")).lower().strip()

#     try:
#         amount = Decimal(str(request.data.get("amount")))
#     except Exception:
#         return Response({"error": "Invalid amount"}, status=400)

#     if amount <= 0:
#         return Response({"error": "Amount must be greater than zero"}, status=400)

#     with transaction.atomic():

#         wallet, _ = Wallet.objects.select_for_update().get_or_create(
#             owner=user,
#             defaults={"amount": Decimal("0.00")}
#         )

#         if wallet.amount < amount:
#             return Response({"error": "Insufficient balance"}, status=400)

#         # -------------------------
#         # Build VTpass payload
#         # -------------------------
#         if product == "airtime":

#             payload = {
#                 "request_id": generate_request_id(),
#                 "serviceID": request.data.get("network"),
#                 "amount": str(amount),
#                 "phone": request.data.get("phone"),
#             }

#         elif product == "data":

#             payload = {
#                 "request_id": generate_request_id(),
#                 "serviceID": request.data.get("network"),
#                 "billersCode": request.data.get("phone"),
#                 "variation_code": request.data.get("variation_code"),
#                 "amount": str(amount),
#                 "phone": request.data.get("phone"),
#             }

#         elif product == "cabletv":

#             payload = {
#                 "request_id": generate_request_id(),
#                 "serviceID": request.data.get("serviceID"),
#                 "billersCode": request.data.get("smartcard_number"),
#                 "variation_code": request.data.get("variation_code"),
#                 "amount": str(amount),
#                 "phone": request.data.get("phone"),
#             }

#         else:
#             return Response({"error": "Invalid product"}, status=400)

#         # -------------------------
#         # Call VTpass
#         # -------------------------
#         data, status_code = vtpass_post(
#             "https://sandbox.vtpass.com/api/pay",
#             payload
#         )

#         if status_code != 200:
#             return Response(data, status=status_code)

#         # -------------------------
#         # Save transaction for webhook
#         # -------------------------
#         Transaction.objects.create(
#             user=user,
#             request_id=payload["request_id"],
#             transaction_id="",
#             product_name=product,
#             phone=request.data.get("phone", ""),
#             amount=amount,
#             total_amount=amount,
#             status="pending",
#             response_code="",
#             response_description="Pending",
#         )

#         # -------------------------
#         # Debit wallet
#         # -------------------------
#         wallet.amount -= amount
#         wallet.save(update_fields=["amount"])

#         return Response({
#             "success": True,
#             "message": "Purchase submitted successfully.",
#             "request_id": payload["request_id"],
#             "product": product,
#             "amount": str(amount),
#             "new_balance": str(wallet.amount),
#             "api_response": data,
#         })














# ======================================================
# 🔥 PRODUCT MAPPING (YOUR SYSTEM LOGIC)
# ======================================================

# ======================================================
# 🔥 MAIN PURCHASE API
# ======================================================

# @api_view(["POST"])
# @permission_classes([IsAuthenticated])
# def buy_product(request):

#     user = request.user

#     product_key = str(request.data.get("product", "")).lower().strip()
#     product = PRODUCT_MAP.get(product_key)

#     if not product:
#         return Response({"error": "Invalid product (use product_1, product_2, product_3)"}, status=400)

#     try:
#         amount = Decimal(str(request.data.get("amount")))
#     except:
#         return Response({"error": "Invalid amount"}, status=400)

#     if amount <= 0:
#         return Response({"error": "Amount must be greater than zero"}, status=400)

#     phone = request.data.get("phone")

#     with transaction.atomic():

#         wallet, _ = Wallet.objects.select_for_update().get_or_create(
#             owner=user,
#             defaults={"amount": Decimal("0.00")}
#         )

#         if wallet.amount < amount:
#             return Response({"error": "Insufficient balance"}, status=400)

#         request_id = generate_request_id()

#         payload = {
#             "request_id": request_id,
#             "amount": str(amount),
#             "phone": phone,
#         }

#         # ======================================================
#         # 🔥 PRODUCT 1: AIRTIME
#         # ======================================================
#         if product == "airtime":

#             network = request.data.get("network")
#             serviceID = VTU_SERVICE_MAP.get(network)

#             if not serviceID:
#                 return Response({"error": "Invalid network"}, status=400)

#             payload.update({
#                 "serviceID": serviceID,
#             })

#         # ======================================================
#         # 🔥 PRODUCT 2: DATA
#         # ======================================================
#         elif product == "data":

#             network = request.data.get("network")
#             serviceID = VTU_SERVICE_MAP.get(f"{network}-data")

#             variation_code = request.data.get("variation_code")

#             if not serviceID:
#                 return Response({"error": "Invalid data network"}, status=400)

#             if not variation_code:
#                 return Response({"error": "variation_code required"}, status=400)

#             payload.update({
#                 "serviceID": serviceID,
#                 "billersCode": phone,
#                 "variation_code": variation_code,
#             })

#         # ======================================================
#         # 🔥 PRODUCT 3: CABLE TV
#         # ======================================================
#         elif product == "cabletv":

#             serviceID = VTU_SERVICE_MAP.get(request.data.get("serviceID"))

#             if not serviceID:
#                 return Response({"error": "Invalid cable service"}, status=400)

#             payload.update({
#                 "serviceID": serviceID,
#                 "billersCode": request.data.get("smartcard_number"),
#                 "variation_code": request.data.get("variation_code"),
#             })

#         # ======================================================
#         # 🔥 CALL VTpass
#         # ======================================================
#         data, status_code = vtpass_post(
#             "https://sandbox.vtpass.com/api/pay",
#             payload
#         )

#         if status_code != 200:
#             return Response(data, status=status_code)

#         # ======================================================
#         # SAVE TRANSACTION
#         # ======================================================
#         Transaction.objects.create(
#             user=user,
#             request_id=request_id,
#             transaction_id="",
#             product_name=product,
#             phone=phone,
#             amount=amount,
#             total_amount=amount,
#             status="pending",
#         )

#         # ======================================================
#         # DEBIT WALLET
#         # ======================================================
#         wallet.amount -= amount
#         wallet.save(update_fields=["amount"])

#         return Response({
#             "success": True,
#             "product": product,
#             "request_id": request_id,
#             "amount": str(amount),
#             "new_balance": str(wallet.amount),
#             "api_response": data,
#         })



from decimal import Decimal
from django.db import transaction
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Wallet, Transaction
from .utils import generate_request_id, vtpass_post


# ======================================================
# PRODUCT MAP
# ======================================================

PRODUCT_MAP = {
    "product_1": "airtime",
    "product_2": "data",
    "product_3": "cabletv",
}


# ======================================================
# VTpass SERVICE MAP
# ======================================================

VTU_SERVICE_MAP = {
    # Airtime
    "mtn": "mtn",
    "airtel": "airtel",
    "glo": "glo",
    "9mobile": "etisalat",
    "intl": "intl",

    # Data
    "mtn-data": "mtn",
    "airtel-data": "airtel",
    "glo-data": "glo",
    "glo-sme": "glo-sme-data",
    "9mobile-data": "etisalat",
    "smile": "smile-direct",
    "spectranet": "spectranet",

    # Cable TV
    "dstv": "dstv",
    "gotv": "gotv",
    "startimes": "startimes",
}


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def buy_product(request):

    user = request.user

    product_key = str(request.data.get("product", "")).lower().strip()
    product = PRODUCT_MAP.get(product_key)

    if not product:
        return Response({"error": "Invalid product"}, status=400)

    try:
        amount = Decimal(str(request.data.get("amount")))
    except Exception:
        return Response({"error": "Invalid amount"}, status=400)

    if amount <= 0:
        return Response({"error": "Amount must be greater than zero"}, status=400)

    phone = request.data.get("phone")

    if not phone:
        return Response({"error": "Phone number is required"}, status=400)

    with transaction.atomic():

        wallet, _ = Wallet.objects.select_for_update().get_or_create(
            owner=user,
            defaults={"amount": Decimal("0.00")}
        )

        if wallet.amount < amount:
            return Response({"error": "Insufficient balance"}, status=400)

        request_id = generate_request_id()

        payload = {
            "request_id": request_id,
            "amount": str(amount),
            "phone": phone,
        }

        # ======================================================
        # AIRTIME
        # ======================================================

        if product == "airtime":

            network = request.data.get("network", "").lower().strip()

            serviceID = VTU_SERVICE_MAP.get(network)

            if not serviceID:
                return Response({"error": "Invalid airtime network"}, status=400)

            payload["serviceID"] = serviceID

        # ======================================================
        # DATA
        # ======================================================

        elif product == "data":

            network = request.data.get("network", "").lower().strip()
            variation_code = request.data.get("variation_code")

            if not network:
                return Response({"error": "Network required"}, status=400)

            if not variation_code:
                return Response({"error": "variation_code required"}, status=400)

            serviceID = VTU_SERVICE_MAP.get(network)

            if not serviceID:
                return Response({"error": "Invalid data network"}, status=400)

            payload.update({
                "serviceID": serviceID,
                "billersCode": phone,
                "variation_code": variation_code,
            })

        # ======================================================
        # CABLE TV
        # ======================================================

        elif product == "cabletv":

            service = request.data.get("serviceID", "").lower().strip()
            variation_code = request.data.get("variation_code")
            smartcard = request.data.get("smartcard_number")

            if not variation_code:
                return Response({"error": "variation_code required"}, status=400)

            if not smartcard:
                return Response({"error": "smartcard_number required"}, status=400)

            serviceID = VTU_SERVICE_MAP.get(service)

            if not serviceID:
                return Response({"error": "Invalid cable service"}, status=400)

            payload.update({
                "serviceID": serviceID,
                "billersCode": smartcard,
                "variation_code": variation_code,
            })

        print("========== FINAL PAYLOAD ==========")
        print(payload)
        print("===================================")

        # ======================================================
        # SEND TO VTPASS
        # ======================================================

        try:
            data, status_code = vtpass_post(
                "https://sandbox.vtpass.com/api/pay",
                payload
            )
        except Exception as e:
            return Response(
                {
                    "error": "Unable to connect to VTpass",
                    "details": str(e)
                },
                status=500
            )

        print("========== VTPASS RESPONSE ==========")
        print(data)
        print("=====================================")

        if status_code != 200:
            return Response(data, status=status_code)

        success = (
            data.get("code") == "000"
            or data.get("response_code") == "000"
            or data.get("response_description", "").lower() == "transaction successful"
            or data.get("content", {})
                .get("transactions", {})
                .get("status", "")
                .lower() == "delivered"
        )

        if not success:

            Transaction.objects.create(
                owner=user,
                amount=amount,
                transaction_type="debit",
                product=product,
                reference=request_id,
                status="failed",
            )

            return Response(data, status=400)

        # ======================================================
        # DEBIT WALLET
        # ======================================================

        wallet.amount -= amount
        wallet.save()

        # ======================================================
        # SAVE TRANSACTION
        # ======================================================

        Transaction.objects.create(
            owner=user,
            amount=amount,
            transaction_type="debit",
            product=product,
            reference=request_id,
            status="successful",
        )

        return Response(
            {
                "message": f"{product.title()} purchase successful",
                "reference": request_id,
                "wallet_balance": str(wallet.amount),
                "vtpass": data,
            },
            status=200,
        )
        
    
# @api_view(["POST"])
# @permission_classes([IsAuthenticated])
# def buy_product(request):

#     user = request.user
#     product = str(request.data.get("product", "")).lower().strip()

#     try:
#         amount = Decimal(str(request.data.get("amount")))
#     except Exception:
#         return Response({"error": "Invalid amount"}, status=400)

#     if amount <= 0:
#         return Response({"error": "Amount must be greater than zero"}, status=400)

#     with transaction.atomic():

#         wallet, _ = Wallet.objects.select_for_update().get_or_create(
#             owner=user,
#             defaults={"amount": Decimal("0.00")}
#         )

#         if wallet.amount < amount:
#             return Response({"error": "Insufficient balance"}, status=400)

#         # -------------------------
#         # Build VTpass payload
#         # -------------------------
#         if product == "airtime":

#             payload = {
#                 "request_id": generate_request_id(),
#                 "serviceID": request.data.get("network"),
#                 "amount": str(amount),
#                 "phone": request.data.get("phone"),
#             }

#         elif product == "data":

#             payload = {
#                 "request_id": generate_request_id(),
#                 "serviceID": request.data.get("network"),
#                 "billersCode": request.data.get("phone"),
#                 "variation_code": request.data.get("variation_code"),
#                 "amount": str(amount),
#                 "phone": request.data.get("phone"),
#             }

#         elif product == "cabletv":

#             payload = {
#                 "request_id": generate_request_id(),
#                 "serviceID": request.data.get("serviceID"),
#                 "billersCode": request.data.get("smartcard_number"),
#                 "variation_code": request.data.get("variation_code"),
#                 "amount": str(amount),
#                 "phone": request.data.get("phone"),
#             }

#         else:
#             return Response({"error": "Invalid product"}, status=400)

#         # -------------------------
#         # Call VTpass
#         # -------------------------
#         data, status_code = vtpass_post(
#             "https://sandbox.vtpass.com/api/pay",
#             payload
#         )

#         if status_code != 200:
#             return Response(data, status=status_code)

#         # -------------------------
#         # Save transaction for webhook
#         # -------------------------
#         Transaction.objects.create(
#             user=user,
#             request_id=payload["request_id"],
#             transaction_id="",
#             product_name=product,
#             phone=request.data.get("phone", ""),
#             amount=amount,
#             total_amount=amount,
#             status="pending",
#             response_code="",
#             response_description="Pending",
#         )

#         # -------------------------
#         # Debit wallet
#         # -------------------------
#         wallet.amount -= amount
#         wallet.save(update_fields=["amount"])

#         return Response({
#             "success": True,
#             "message": "Purchase submitted successfully.",
#             "request_id": payload["request_id"],
#             "product": product,
#             "amount": str(amount),
#             "new_balance": str(wallet.amount),
#             "api_response": data,
#         })
from decimal import Decimal
import logging

from django.db import transaction as db_transaction
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Transaction, Wallet

logger = logging.getLogger(__name__)


@api_view(["POST"])
@permission_classes([AllowAny])
def vtpass_webhook(request):

    payload = request.data
    logger.info("VTpass Webhook RAW: %s", payload)

    # =========================
    # STEP 1: VALIDATE TYPE
    # =========================
    if payload.get("type") != "transaction-update":
        logger.warning("Ignored webhook type: %s", payload.get("type"))
        return Response({"response": "ignored"})

    data = payload.get("data") or {}

    content = data.get("content") or {}
    trx = content.get("transactions") or {}

    # =========================
    # STEP 2: IDs (CORRECT VTpass format)
    # =========================
    request_id = data.get("requestId")

    transaction_id = trx.get("transactionId")

    if not request_id:
        logger.warning("Missing requestId")
        return Response({"response": "success"})

    request_id = str(request_id).strip()

    logger.info("RequestId=%s | TransactionId=%s", request_id, transaction_id)

    try:
        with db_transaction.atomic():

            # =========================
            # STEP 3: FIND TRANSACTION (STRICT FIRST)
            # =========================
            txn = Transaction.objects.select_for_update().filter(
                request_id=request_id
            ).first()

            # fallback match
            if not txn and transaction_id:
                txn = Transaction.objects.select_for_update().filter(
                    transaction_id=transaction_id
                ).first()

            if not txn:
                logger.warning(
                    "Transaction NOT FOUND request_id=%s tx_id=%s",
                    request_id,
                    transaction_id
                )
                return Response({"response": "success"})

            # =========================
            # STEP 4: CORRECT STATUS PATH
            # =========================
            status = trx.get("status")  # 👈 THIS IS CORRECT PLACE
            if not status:
                status = "pending"

            status = str(status).lower().strip()
            txn.status = status

            # =========================
            # STEP 5: UPDATE FIELDS
            # =========================
            txn.transaction_id = transaction_id or txn.transaction_id
            txn.product_name = trx.get("product_name") or txn.product_name
            txn.phone = trx.get("phone") or txn.phone
            txn.email = trx.get("email") or txn.email

            def to_decimal(v):
                try:
                    return Decimal(str(v))
                except:
                    return None

            amt = to_decimal(trx.get("amount"))
            if amt:
                txn.amount = amt

            txn.total_amount = to_decimal(trx.get("total_amount")) or txn.total_amount

            txn.response_description = data.get("response_description") or txn.response_description

            txn.save()

            # =========================
            # STEP 6: HANDLE REVERSAL
            # =========================
            if status in ["reversed"] and not txn.reversed:

                wallet = Wallet.objects.select_for_update().get(owner=txn.user)

                wallet.amount += txn.amount or Decimal("0")
                wallet.save(update_fields=["amount"])

                txn.reversed = True
                txn.save(update_fields=["reversed"])

                logger.info("Refunded %s to %s", txn.amount, txn.user)

            logger.info("UPDATED %s => %s", txn.request_id, txn.status)

    except Exception as e:
        logger.exception("VTpass webhook error: %s", e)

    return Response({"response": "success"})