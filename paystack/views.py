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
#     request_id=reference
# ).first()
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

#     # Transaction.objects.create(
#     #     user=user,
#     #     reference=reference,
#     #     amount=amount,
#     #     status="success",
#     #     email=payment["customer"]["email"]
#     # )
#     Transaction.objects.create(
#     user=user,
#     request_id=reference,
#     amount=amount,
#     status="success",
#     email=payment["customer"]["email"]
# )
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

from .models import Wallet, Transaction, VariationCode


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


# from decimal import Decimal

# from django.db import transaction

# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response

# from .models import Wallet, Transaction, VariationCode


# # ======================================================
# # PRODUCT MAPPING
# # ======================================================

# PRODUCT_MAP = {
#     "product_1": "airtime",
#     "product_2": "data",
#     "product_3": "cabletv",
# }


# # ======================================================
# # VTpass SERVICE MAP
# # ======================================================

# VTU_SERVICE_MAP = {

#     # Airtime
#     "mtn": "mtn",
#     "airtel": "airtel",
#     "glo": "glo",
#     "9mobile": "etisalat",
#     "intl": "intl",


#     # Data
#     "mtn-data": "mtn-data",
#     "airtel-data": "airtel-data",
#     "glo-data": "glo-data",
#     "glo-sme-data": "glo-sme-data",
#     "9mobile-data": "etisalat-data",
#     "smile-data": "smile-direct",
#     "spectranet-data": "spectranet",


#     # Cable
#     "dstv": "dstv",
#     "gotv": "gotv",
#     "startimes": "startimes",
# }



# @api_view(["POST"])
# @permission_classes([IsAuthenticated])
# def buy_product(request):

#     user = request.user


#     product_key = str(
#         request.data.get("product","")
#     ).lower().strip()


#     product = PRODUCT_MAP.get(product_key)



#     if not product:

#         return Response(
#             {
#                 "error":"Invalid product"
#             },
#             status=400
#         )



#     try:

#         amount = Decimal(
#             str(request.data.get("amount"))
#         )

#     except:

#         return Response(
#             {
#                 "error":"Invalid amount"
#             },
#             status=400
#         )



#     phone = str(
#         request.data.get("phone","")
#     ).strip()



#     with transaction.atomic():



#         wallet, _ = Wallet.objects.select_for_update().get_or_create(
#             owner=user,
#             defaults={
#                 "amount":Decimal("0.00")
#             }
#         )



#         if wallet.amount < amount:

#             return Response(
#                 {
#                     "error":"Insufficient balance"
#                 },
#                 status=400
#             )



#         request_id = generate_request_id()



#         payload = {

#             "request_id":request_id,

#             "amount":str(amount),

#             "phone":phone,

#         }



#         service_name = ""



#         # ======================================================
#         # AIRTIME
#         # ======================================================

#         if product == "airtime":


#             network = str(
#                 request.data.get("network","")
#             ).lower().strip()



#             service_id = VTU_SERVICE_MAP.get(
#                 network
#             )


#             if not service_id:

#                 return Response(
#                     {
#                         "error":"Invalid network"
#                     },
#                     status=400
#                 )



#             service_name = (
#                 f"{network.upper()} Airtime VTU"
#             )



#             payload.update({

#                 "serviceID":service_id

#             })




#         # ======================================================
#         # DATA
#         # ======================================================

#         elif product == "data":


#             network = str(
#                 request.data.get("network","")
#             ).lower().strip()



#             variation_code = request.data.get(
#                 "variation_code"
#             )



#             service_id = VTU_SERVICE_MAP.get(
#                 f"{network}-data"
#             )



#             if not service_id:

#                 return Response(
#                     {
#                         "error":"Invalid data network"
#                     },
#                     status=400
#                 )



#             if not variation_code:

#                 return Response(
#                     {
#                         "error":"variation_code required"
#                     },
#                     status=400
#                 )




#             try:

#                 variation = VariationCode.objects.get(
#                     variation_code=variation_code
#                 )


#                 service_name = (
#                     f"{network.upper()} Data - {variation.name}"
#                 )


#             except VariationCode.DoesNotExist:


#                 service_name = (
#                     f"{network.upper()} Data Bundle"
#                 )




#             payload.update({

#                 "serviceID":service_id,

#                 "billersCode":phone,

#                 "variation_code":variation_code,

#             })






#         # ======================================================
#         # SEND TO VTPASS
#         # ======================================================


#         print("==========================")
#         print("PAYLOAD:",payload)
#         print("==========================")



#         data, status_code = vtpass_post(

#             "https://sandbox.vtpass.com/api/pay",

#             payload

#         )



#         print("VTPASS RESPONSE:",data)



#         if status_code != 200:

#             return Response(
#                 data,
#                 status=status_code
#             )



#         if data.get("code") != "000":

#             return Response(
#                 data,
#                 status=400
#             )




#         transaction_data = {}



#         if isinstance(
#             data.get("content"),
#             dict
#         ):

#             transaction_data = (
#                 data["content"]
#                 .get(
#                     "transactions",
#                     {}
#                 )
#             )




#         # ======================================================
#         # USE VTPASS REAL NAME
#         # ======================================================


#         vtpass_product_name = transaction_data.get(
#             "product_name"
#         )



#         if vtpass_product_name:

#             service_name = vtpass_product_name





#         # ======================================================
#         # SAVE TRANSACTION
#         # ======================================================


#         Transaction.objects.create(

#             user=user,


#             request_id=request_id,


#             transaction_id=transaction_data.get(
#                 "transactionId",
#                 ""
#             ),


#             product_name=service_name,


#             phone=phone,


#             amount=amount,


#             total_amount=amount,


#             status=transaction_data.get(
#                 "status",
#                 "delivered"
#             ),


#         )



#         # Remove money

#         wallet.amount -= amount


#         wallet.save(
#             update_fields=[
#                 "amount"
#             ]
#         )




#         return Response({

#             "success":True,


#             "product":product,


#             "service_name":service_name,


#             "request_id":request_id,


#             "transaction_id":transaction_data.get(
#                 "transactionId",
#                 ""
#             ),


#             "amount":str(amount),


#             "new_balance":str(
#                 wallet.amount
#             )


#         })

# from decimal import Decimal

# from django.db import transaction

# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response

# from .models import Wallet, Transaction, VariationCode



# # ======================================================
# # PRODUCT MAPPING
# # ======================================================

# PRODUCT_MAP = {
#     "product_1": "airtime",
#     "product_2": "data",
#     "product_3": "cabletv",
# }



# # ======================================================
# # VTpass SERVICE MAP
# # ======================================================

# VTU_SERVICE_MAP = {

#     "mtn": "mtn",
#     "airtel": "airtel",
#     "glo": "glo",
#     "9mobile": "etisalat",

#     "mtn-data": "mtn-data",
#     "airtel-data": "airtel-data",
#     "glo-data": "glo-data",
#     "9mobile-data": "etisalat-data",

#     "dstv": "dstv",
#     "gotv": "gotv",
#     "startimes": "startimes",

# }



# @api_view(["POST"])
# @permission_classes([IsAuthenticated])
# def buy_product(request):

#     user = request.user


#     product_key = str(
#         request.data.get("product", "")
#     ).lower().strip()


#     product = PRODUCT_MAP.get(product_key)


#     if not product:

#         return Response(
#             {
#                 "error": "Invalid product"
#             },
#             status=400
#         )


#     try:

#         amount = Decimal(
#             str(
#                 request.data.get("amount")
#             )
#         )

#     except:

#         return Response(
#             {
#                 "error":"Invalid amount"
#             },
#             status=400
#         )



#     phone = str(
#         request.data.get("phone","")
#     ).strip()



#     variation_code = ""

#     variation_name = ""

#     service_name = ""



#     with transaction.atomic():



#         wallet, _ = Wallet.objects.select_for_update().get_or_create(
#             owner=user,
#             defaults={
#                 "amount": Decimal("0.00")
#             }
#         )



#         if wallet.amount < amount:

#             return Response(
#                 {
#                     "error":"Insufficient balance"
#                 },
#                 status=400
#             )



#         request_id = generate_request_id()



#         payload = {

#             "request_id": request_id,

#             "amount": str(amount),

#             "phone": phone,

#         }



#         # ==========================
#         # AIRTIME
#         # ==========================

#         if product == "airtime":


#             network = str(
#                 request.data.get("network","")
#             ).lower().strip()



#             service_id = VTU_SERVICE_MAP.get(
#                 network
#             )


#             if not service_id:

#                 return Response(
#                     {
#                         "error":"Invalid network"
#                     },
#                     status=400
#                 )


#             service_name = (
#                 f"{network.upper()} Airtime"
#             )


#             payload.update({

#                 "serviceID":service_id

#             })



#         # ==========================
#         # DATA
#         # ==========================

#         elif product == "data":


#             network = str(
#                 request.data.get("network","")
#             ).lower().strip()



#             variation_code = str(
#                 request.data.get(
#                     "variation_code",
#                     ""
#                 )
#             )



#             service_id = VTU_SERVICE_MAP.get(
#                 f"{network}-data"
#             )


#             if not service_id:

#                 return Response(
#                     {
#                         "error":"Invalid data network"
#                     },
#                     status=400
#                 )


#             if not variation_code:

#                 return Response(
#                     {
#                         "error":"variation_code required"
#                     },
#                     status=400
#                 )



#             try:

#                 variation = VariationCode.objects.get(
#                     variation_code=variation_code
#                 )

#                 variation_name = variation.name


#             except VariationCode.DoesNotExist:

#                 variation_name = "Data Bundle"



#             service_name = (
#                 f"{network.upper()} Data - {variation_name}"
#             )



#             payload.update({

#                 "serviceID":service_id,

#                 "billersCode":phone,

#                 "variation_code":variation_code,

#             })




#         print("==========================")
#         print("PAYLOAD:",payload)
#         print("==========================")



#         data, status_code = vtpass_post(
#             "https://sandbox.vtpass.com/api/pay",
#             payload
#         )



#         print("VTPASS RESPONSE:",data)



#         if status_code != 200:

#             return Response(
#                 data,
#                 status=status_code
#             )



#         if data.get("code") != "000":

#             return Response(
#                 data,
#                 status=400
#             )



#         transaction_data = {}


#         if isinstance(
#             data.get("content"),
#             dict
#         ):

#             transaction_data = (
#                 data["content"]
#                 .get(
#                     "transactions",
#                     {}
#                 )
#             )



#         # Use VTpass product name

#         if transaction_data.get("product_name"):

#             service_name = transaction_data.get(
#                 "product_name"
#             )



#         commission = Decimal(
#             str(
#                 transaction_data.get(
#                     "commission",
#                     0
#                 )
#             )
#         )



#         # ==========================
#         # SAVE TRANSACTION
#         # ==========================


#         Transaction.objects.create(

#             user=user,

#             request_id=request_id,

#             transaction_id=transaction_data.get(
#                 "transactionId",
#                 ""
#             ),


#             service=product,


#             product_name=service_name,


#             variation_code=variation_code,


#             variation_name=variation_name,


#             phone=phone,


#             amount=amount,


#             total_amount=amount,


#             commission=commission,


#             status=transaction_data.get(
#                 "status",
#                 "delivered"
#             ),


#         )



#         # Deduct wallet

#         wallet.amount -= amount


#         wallet.save(
#             update_fields=[
#                 "amount"
#             ]
#         )



#         return Response({

#             "success":True,

#             "product":product,

#             "service_name":service_name,

#             "variation_code":variation_code,

#             "variation_name":variation_name,

#             "request_id":request_id,

#             "transaction_id":transaction_data.get(
#                 "transactionId",
#                 ""
#             ),

#             "amount":str(amount),

#             "commission":str(commission),

#             "new_balance":str(
#                 wallet.amount
#             )

#         })
# from decimal import Decimal
# from django.db import transaction

# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
# from .models import Wallet, Transaction, VariationCode

# @api_view(["POST"])
# @permission_classes([IsAuthenticated])
# def buy_product(request):

#     print("BUY PRODUCT STARTED")
#     print("USER:", request.user)
#     print("DATA:", request.data)


#     user = request.user

#     product_key = str(request.data.get("product", "")).lower().strip()
#     product = PRODUCT_MAP.get(product_key)

#     if not product:
#         return Response({"error": "Invalid product"}, status=400)

#     try:
#         amount = Decimal(str(request.data.get("amount")))
#     except Exception:
#         return Response({"error": "Invalid amount"}, status=400)

#     phone = str(request.data.get("phone", "")).strip()

#     variation = None
#     variation_code = ""
#     variation_name = ""
#     service_name = ""

#     with transaction.atomic():

#         wallet, _ = Wallet.objects.select_for_update().get_or_create(
#             owner=user,
#             defaults={"amount": Decimal("0.00")}
#         )

#         if wallet.amount < amount:
#             return Response(
#                 {"error": "Insufficient balance"},
#                 status=400
#             )

#         request_id = generate_request_id()

#         payload = {
#             "request_id": request_id,
#             "amount": str(amount),
#             "phone": phone,
#         }

#         # =========================
#         # AIRTIME
#         # =========================
#         if product == "airtime":

#             network = str(request.data.get("network", "")).lower().strip()

#             service_id = VTU_SERVICE_MAP.get(network)

#             if not service_id:
#                 return Response({"error": "Invalid network"}, status=400)

#             service_name = f"{network.upper()} Airtime"

#             payload.update({
#                 "serviceID": service_id,
#             })

#         # =========================
#         # DATA
#         # =========================
#         elif product == "data":

#             network = str(request.data.get("network", "")).lower().strip()

#             variation_code = str(
#                 request.data.get("variation_code", "")
#             ).strip()

#             service_id = VTU_SERVICE_MAP.get(f"{network}-data")

#             if not service_id:
#                 return Response(
#                     {"error": "Invalid data network"},
#                     status=400
#                 )

#             if not variation_code:
#                 return Response(
#                     {"error": "variation_code required"},
#                     status=400
#                 )

#             variation = VariationCode.objects.filter(
#                 variation_code=variation_code
#             ).first()

#             variation_name = (
#                 variation.name if variation else "Data Bundle"
#             )

#             service_name = (
#                 f"{network.upper()} Data - {variation_name}"
#             )

#             payload.update({
#                 "serviceID": service_id,
#                 "billersCode": phone,
#                 "variation_code": variation_code,
#             })

#         # =========================
#         # CABLE TV
#         # =========================
#         elif product == "cabletv":

#             provider = str(
#                 request.data.get("provider", "")
#             ).lower().strip()

#             service_id = VTU_SERVICE_MAP.get(provider)

#             if not service_id:
#                 return Response(
#                     {"error": "Invalid cable provider"},
#                     status=400
#                 )

#             variation_code = str(
#                 request.data.get("variation_code", "")
#             ).strip()

#             if not variation_code:
#                 return Response(
#                     {"error": "variation_code required"},
#                     status=400
#                 )

#             decoder_number = str(
#                 request.data.get("decoder_number", "")
#             ).strip()

#             if not decoder_number:
#                 return Response(
#                     {"error": "decoder_number required"},
#                     status=400
#                 )

#             subscription_type = str(
#                 request.data.get(
#                     "subscription_type",
#                     "change"
#                 )
#             ).lower().strip()

#             if subscription_type not in ["change", "renew"]:
#                 return Response(
#                     {
#                         "error": "subscription_type must be change or renew"
#                     },
#                     status=400
#                 )

#             variation = VariationCode.objects.filter(
#                 variation_code=variation_code
#             ).first()

#             variation_name = (
#                 variation.name if variation else "Cable Subscription"
#             )

#             service_name = (
#                 f"{provider.upper()} - {variation_name}"
#             )

#             payload.update({
#                 "serviceID": service_id,
#                 "billersCode": decoder_number,
#                 "variation_code": variation_code,
#                 "subscription_type": subscription_type,
#                 "phone": phone,
#                 "amount": str(amount),
#             })

#         # =========================
#         # CALL VTPASS
#         # =========================

#         print("PAYLOAD:", payload)

#         data, status_code = vtpass_post(
#             "https://sandbox.vtpass.com/api/pay",
#             payload
#         )

#         print("VTPASS RESPONSE:", data)

#         if status_code != 200:
#             return Response(data, status=status_code)

#         if data.get("code") != "000":
#             return Response(data, status=400)

#         transaction_data = {}

#         if isinstance(data.get("content"), dict):
#             transaction_data = data["content"].get(
#                 "transactions",
#                 {}
#             )

#         if transaction_data.get("product_name"):
#             service_name = transaction_data["product_name"]

#         commission = Decimal(
#             str(transaction_data.get("commission", "0"))
#         )

#         # =========================
#         # SAVE TRANSACTION
#         # =========================

#         Transaction.objects.create(
#             user=user,
#             request_id=request_id,
#             transaction_id=transaction_data.get(
#                 "transactionId",
#                 ""
#             ),
#             service=product,
#             product_name=service_name,
#             variation=variation,
#             phone=phone,
#             amount=amount,
#             total_amount=amount,
#             commission=commission,
#             status=transaction_data.get(
#                 "status",
#                 "delivered"
#             ),
#         )

#         # =========================
#         # DEDUCT WALLET
#         # =========================

#         wallet.amount -= amount
#         wallet.save(update_fields=["amount"])

#         return Response({
#             "success": True,
#             "product": product,
#             "service_name": service_name,
#             "variation_code": variation_code,
#             "variation_name": variation_name,
#             "request_id": request_id,
#             "transaction_id": transaction_data.get(
#                 "transactionId",
#                 ""
#             ),
#             "amount": str(amount),
#             "commission": str(commission),
#             "new_balance": str(wallet.amount),
#         })


# ======================================================
# PRODUCT MAPPING
# ======================================================
from decimal import Decimal
import traceback

from django.db import transaction

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Wallet, Transaction, VariationCode



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

    "mtn": "mtn",
    "airtel": "airtel",
    "glo": "glo",
    "9mobile": "etisalat",

    "mtn-data": "mtn-data",
    "airtel-data": "airtel-data",
    "glo-data": "glo-data",
    "9mobile-data": "etisalat-data",

    "dstv": "dstv",
    "gotv": "gotv",
    "startimes": "startimes",

}



# ======================================================
# BUY PRODUCT
# ======================================================

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def buy_product(request):

    try:

        print("BUY PRODUCT STARTED")
        print("USER:", request.user)
        print("DATA:", request.data)



        user = request.user



        product_key = str(
            request.data.get("product","")
        ).lower().strip()



        product = PRODUCT_MAP.get(product_key)



        if not product:

            return Response(
                {
                    "Invalid product"
                },
                status=400
            )




        try:

            amount = Decimal(
                str(
                    request.data.get("amount")
                )
            )

        except:

            return Response(
                {
                    "error":"Invalid amount"
                },
                status=400
            )





        phone = str(
            request.data.get("phone","")
        ).strip()



        if not phone:

            return Response(
                {
                    "Phone required"
                },
                status=400
            )




        variation = None
        variation_code = ""
        variation_name = ""
        service_name = ""




        with transaction.atomic():
            wallet, created = Wallet.objects.select_for_update().get_or_create(

    user=user,

    defaults={
        "balance": Decimal("0.00")
    }

)

            # wallet, created = Wallet.objects.select_for_update().get_or_create(

            #     owner=user,

            #     defaults={
            #         "amount":Decimal("0.00")
            #     }

            # )
            if wallet.balance < amount:
            # if wallet.amount < amount:

                return Response(
                    {
                        "Insufficient balance"
                    },
                    status=400
                )




            request_id = generate_request_id()



            payload = {

                "request_id":request_id,

                "amount":str(amount),

                "phone":phone,

            }





            # ==========================
            # AIRTIME
            # ==========================

            if product == "airtime":


                network = str(
                    request.data.get("network","")
                ).lower().strip()



                service_id = VTU_SERVICE_MAP.get(
                    network
                )



                if not service_id:

                    return Response(
                        {
                            "Invalid network"
                        },
                        status=400
                    )



                service_name = (
                    network.upper()
                    +
                    " Airtime"
                )



                payload["serviceID"] = service_id





            # ==========================
            # DATA
            # ==========================

            elif product == "data":



                network = str(
                    request.data.get("network","")
                ).lower().strip()



                variation_code = str(
                    request.data.get(
                        "variation_code",
                        ""
                    )
                ).strip()



                if not variation_code:

                    return Response(
                        {
                            "variation_code required"
                        },
                        status=400
                    )




                service_id = VTU_SERVICE_MAP.get(

                    f"{network}-data"

                )



                if not service_id:

                    return Response(
                        {
                            "Invalid data network"
                        },
                        status=400
                    )




                variation = VariationCode.objects.filter(

                    variation_code=variation_code

                ).first()




                variation_name = (

                    variation.name

                    if variation

                    else

                    "Data Bundle"

                )




                service_name = (

                    f"{network.upper()} Data - {variation_name}"

                )




                payload.update({

                    "serviceID":service_id,

                    "billersCode":phone,

                    "variation_code":variation_code

                })






            # ==========================
            # CABLE TV
            # ==========================

            elif product == "cabletv":



                provider = str(

                    request.data.get(

                        "provider",

                        request.data.get(

                            "serviceID",

                            ""

                        )

                    )

                ).lower().strip()




                service_id = VTU_SERVICE_MAP.get(
                    provider
                )



                if not service_id:

                    return Response(
                        {
                            "Invalid provider"
                        },
                        status=400
                    )




                variation_code = str(

                    request.data.get(

                        "variation_code",

                        ""

                    )

                ).strip()




                if not variation_code:

                    return Response(
                        {
                            "variation_code required"
                        },
                        status=400
                    )




                variation = VariationCode.objects.filter(

                    variation_code=variation_code

                ).first()




                variation_name = (

                    variation.name

                    if variation

                    else

                    "Subscription"

                )




                service_name = (

                    f"{provider.upper()} - {variation_name}"

                )




                decoder = request.data.get(

                    "smartcard_number",

                    request.data.get(

                        "decoder_number"

                    )

                )




                if not decoder:

                    return Response(
                        {
                            "Smartcard number required"
                        },
                        status=400
                    )




                payload.update({

                    "serviceID":service_id,

                    "billersCode":decoder,

                    "variation_code":variation_code

                })






            else:


                return Response(
                    {
                        "Unsupported product"
                    },
                    status=400
                )







            print("VTPASS PAYLOAD:",payload)



            data, status_code = vtpass_post(

                "https://sandbox.vtpass.com/api/pay",

                payload

            )



            print("VTPASS RESPONSE:",data)





            if status_code != 200:

                return Response(
                    data,
                    status=status_code
                )




            if data.get("code") != "000":

                return Response(
                    data,
                    status=400
                )





            transaction_data = {}



            if isinstance(data.get("content"),dict):

                transaction_data = (

                    data["content"]

                    .get(
                        "transactions",
                        {}
                    )

                )





            commission = Decimal(

                str(

                    transaction_data.get(

                        "commission",

                        "0"

                    )

                )

            )





            Transaction.objects.create(

                user=user,

                request_id=request_id,

                transaction_id=transaction_data.get(

                    "transactionId",

                    ""

                ),

                service=product,

                product_name=service_name,

                variation=variation,

                phone=phone,

                amount=amount,

                total_amount=amount,

                commission=commission,

                status=transaction_data.get(

                    "status",

                    "delivered"

                )

            )
            wallet.balance -= amount
            # wallet.amount -= amount


            wallet.save(

                update_fields=[

                   "balance"

                ]

            )





            return Response({

                "success":True,

                "product":product,

                "service_name":service_name,

                "variation_code":variation_code,

                "variation_name":variation_name,

                "transaction_id":transaction_data.get(

                    "transactionId",

                    ""

                ),

                "amount":str(amount),

                "commission":str(commission),
                "new_balance":str(wallet.balance)
                # "new_balance":str(wallet.amount)

            })





    except Exception as e:


        print("BUY PRODUCT ERROR")

        traceback.print_exc()



        return Response(

            {
                str(e)
            },

            status=500

        )
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










# paystack

import json
import requests
from decimal import Decimal

from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Wallet, VirtualAccount


# ==========================
# CREATE VIRTUAL ACCOUNT
# ==========================

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_virtual_account(request):

    user = request.user

    # Already created
    account = VirtualAccount.objects.filter(user=user).first()

    if account:
        return Response({
            "message": "Virtual account already exists",
            "bank_name": account.bank_name,
            "account_name": account.account_name,
            "account_number": account.account_number,
        })

    headers = {
        "Authorization": f"Bearer {settings.PAYSTACK_SECRET_KEY}",
        "Content-Type": "application/json",
    }

    # --------------------------
    # Create Customer
    # --------------------------

    customer_response = requests.post(
        "https://api.paystack.co/customer",
        headers=headers,
        json={
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
        },
    ).json()

    if not customer_response.get("status"):
        return Response(
            customer_response,
            status=400
        )

    customer_code = customer_response["data"]["customer_code"]

    # --------------------------
    # Create Dedicated Account
    # --------------------------

    account_response = requests.post(
        "https://api.paystack.co/dedicated_account",
        headers=headers,
        json={
            "customer": customer_code,
            "preferred_bank": "wema-bank",
        },
    ).json()

    if not account_response.get("status"):
        return Response(
            account_response,
            status=400
        )

    data = account_response["data"]

    account = VirtualAccount.objects.create(
        user=user,
        customer_code=customer_code,
        bank_name=data["bank"]["name"],
        account_name=data["account_name"],
        account_number=data["account_number"],
    )

    Wallet.objects.get_or_create(user=user)

    return Response({
        "message": "Virtual account created successfully",
        "bank_name": account.bank_name,
        "account_name": account.account_name,
        "account_number": account.account_number,
    })


# ==========================
# WALLET DETAILS
# ==========================

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def wallet(request):

    wallet, _ = Wallet.objects.get_or_create(
        user=request.user
    )

    account = VirtualAccount.objects.filter(
        user=request.user
    ).first()

    return Response({
        "balance": wallet.balance,
        "bank_name": account.bank_name if account else None,
        "account_name": account.account_name if account else None,
        "account_number": account.account_number if account else None,
    })


# ==========================
# PAYSTACK WEBHOOK
# ==========================

@csrf_exempt
def paystack_webhook(request):

    if request.method != "POST":
        return HttpResponse(status=405)

    try:
        payload = json.loads(request.body)

        event = payload.get("event")

        # Money received
        if event == "charge.success":

            data = payload["data"]

            amount = Decimal(str(data["amount"])) / Decimal("100")

            account_number = (
                data.get("authorization", {})
                .get("receiver_bank_account_number")
            )

            if account_number:

                account = VirtualAccount.objects.filter(
                    account_number=account_number
                ).first()

                if account:

                    wallet, _ = Wallet.objects.get_or_create(
                        user=account.user
                    )

                    wallet.balance += amount
                    wallet.save()

        return HttpResponse(status=200)

    except Exception as e:

        print(e)

        return HttpResponse(status=400)