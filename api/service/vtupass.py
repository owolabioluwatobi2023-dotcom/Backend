# import requests
# from django.conf import settings

# def buy_airtime(request_id, phone, amount):
#     url = "https://vtpass.com/api/pay"

#     payload = {
#         "request_id": request_id,
#         "serviceID": "mtn",
#         "amount": amount,
#         "phone": phone
#     }

#     headers = {
#         "api-key": settings.VTPASS_API_KEY,
#         "secret-key": settings.VTPASS_SECRET_KEY
#     }

#     response = requests.post(url, json=payload, headers=headers)
#     return response.json()



import requests
from django.conf import settings

def buy_airtime(request_id, phone, amount, service_id):
    url = "https://vtpass.com/api/pay"

    payload = {
        "request_id": request_id,
        "serviceID": service_id,
        "amount": amount,
        "phone": phone
    }

    headers = {
        "api-key": settings.VTPASS_API_KEY,
        "secret-key": settings.VTPASS_SECRET_KEY,
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    return response.json()



import requests

# def buy_airtime(request_id, phone, amount, service_id):
#     return {
#         "request_id": request_id,
#         "phone": phone,
#         "amount": amount,
#         "service_id": service_id
#     }


import base64
from django.conf import settings

def vtpass_headers():
    auth = f"{settings.VTPASS_USERNAME}:{settings.VTPASS_PASSWORD}"
    encoded = base64.b64encode(auth.encode()).decode()

    return {
        "Content-Type": "application/json",
        "Authorization": f"Basic {encoded}"
    }