# import os
# import json
# import firebase_admin

# from firebase_admin import credentials, messaging


# if not firebase_admin._apps:

#     if os.path.exists("firebase-service-account.json"):

#         cred = credentials.Certificate(
#             "firebase-service-account.json"
#         )

#         firebase_admin.initialize_app(cred)

#         print("🔥 Firebase initialized successfully")

#     else:
#         print("❌ firebase-service-account.json not found")


# def send_push_notification(token, title, body, data=None):

#     message = messaging.Message(
#         notification=messaging.Notification(
#             title=title,
#             body=body,
#         ),
#         token=token,
#         data=data or {},
#     )

#     response = messaging.send(message)

#     return response





import os
import json
import firebase_admin

from firebase_admin import credentials, messaging


# Initialize Firebase only once
if not firebase_admin._apps:

    firebase_json = os.environ.get("FIREBASE_CREDENTIALS")

    if firebase_json:

        try:
            cred = credentials.Certificate(
                json.loads(firebase_json)
            )

            firebase_admin.initialize_app(cred)

            print("🔥 Firebase initialized successfully")

        except Exception as e:
            print("❌ Firebase initialization failed:", e)

    else:
        print("❌ FIREBASE_CREDENTIALS environment variable missing")


def send_push_notification(token, title, body, data=None):

    try:

        message = messaging.Message(

            notification=messaging.Notification(
                title=title,
                body=body,
            ),

            token=token,

            data=data or {}
        )

        response = messaging.send(message)

        return response


    except Exception as e:

        print("❌ Push notification failed:", e)

        return None