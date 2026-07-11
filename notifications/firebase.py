# import firebase_admin
# from firebase_admin import credentials
# import os


# BASE_DIR = os.path.dirname(
#     os.path.dirname(
#         os.path.abspath(__file__)
#     )
# )


# firebase_key = os.path.join(
#     BASE_DIR,
#     "firebase-service-account.json"
# )


# if not firebase_admin._apps:
#     cred = credentials.Certificate(firebase_key)
#     firebase_admin.initialize_app(cred)


# import firebase_admin
# from firebase_admin import credentials, messaging
# import os


# BASE_DIR = os.path.dirname(
#     os.path.dirname(
#         os.path.abspath(__file__)
#     )
# )


# firebase_key = os.path.join(
#     BASE_DIR,
#     "firebase-service-account.json"
# )


# if not firebase_admin._apps:
#     cred = credentials.Certificate(firebase_key)
#     firebase_admin.initialize_app(cred)



# def send_push_notification(user, title, body):

#     from .models import DeviceToken

#     tokens = DeviceToken.objects.filter(
#         user=user
#     )


#     for device in tokens:

#         message = messaging.Message(

#             notification=messaging.Notification(
#                 title=title,
#                 body=body
#             ),

#             token=device.token

#         )


#         try:
#             messaging.send(message)

#         except Exception as e:
#             print("Firebase error:", e)


import os
import json
import firebase_admin
from firebase_admin import credentials


if not firebase_admin._apps:

    firebase_json = os.environ.get("FIREBASE_CREDENTIALS")

    if firebase_json:
        cred = credentials.Certificate(
            json.loads(firebase_json)
        )

        firebase_admin.initialize_app(cred)