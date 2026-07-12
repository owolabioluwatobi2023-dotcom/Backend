# import os
# import json
# import firebase_admin

# from firebase_admin import credentials, messaging


# # Initialize Firebase only once
# if not firebase_admin._apps:

#     firebase_json = os.environ.get("FIREBASE_CREDENTIALS")

#     if firebase_json:

#         try:
#             cred = credentials.Certificate(
#                 json.loads(firebase_json)
#             )

#             firebase_admin.initialize_app(cred)

#             print("🔥 Firebase initialized successfully")

#         except Exception as e:
#             print("❌ Firebase initialization failed:", e)

#     else:
#         print("❌ FIREBASE_CREDENTIALS environment variable missing")


# def send_push_notification(token, title, body, data=None):

#     try:

#         message = messaging.Message(

#             notification=messaging.Notification(
#                 title=title,
#                 body=body,
#             ),

#             token=token,

#             data=data or {}
#         )

#         response = messaging.send(message)

#         return response


#     except Exception as e:

#         print("❌ Push notification failed:", e)

# #         return None

# import os
# import json
# import firebase_admin

# from firebase_admin import credentials, messaging



# if not firebase_admin._apps:

#     firebase_json = os.getenv("FIREBASE_SERVICE_ACCOUNT")

#     if firebase_json:

#         try:
#             cred = credentials.Certificate(
#                 json.loads(firebase_json)
#             )

#             firebase_admin.initialize_app(cred)

#             print("🔥 Firebase initialized successfully")

#         except Exception as e:
#             print("❌ Firebase initialization error:", e)

#     else:
#         print("❌ FIREBASE_SERVICE_ACCOUNT environment variable missing")


# def send_push_notification(token, title, body, data=None):
#     try:
#         message = messaging.Message(
#             notification=messaging.Notification(
#                 title=title,
#                 body=body,
#             ),
#             token=token,
#             data=data or {},
#         )

#         response = messaging.send(message)
#         print("✅ Firebase Response:", response)
#         return response

#     except Exception as e:
#         print("❌ Firebase Error:", e)
#         raise

# # def send_push_notification(token, title, body, data=None):

# #     message = messaging.Message(
# #         notification=messaging.Notification(
# #             title=title,
# #             body=body,
# #         ),
# #         token=token,
# #         data=data or {},
# #     )

# #     response = messaging.send(message)

# #     return response









import os
import json
import firebase_admin

from firebase_admin import credentials, messaging



if not firebase_admin._apps:

    firebase_json = os.getenv("FIREBASE_SERVICE_ACCOUNT")

    if firebase_json:

        try:
            cred = credentials.Certificate(
                json.loads(firebase_json)
            )

            firebase_admin.initialize_app(cred)

            print("🔥 Firebase initialized successfully")

        except Exception as e:
            print("❌ Firebase initialization error:", e)

    else:
        print("❌ FIREBASE_SERVICE_ACCOUNT environment variable missing")
def send_push_notification(token, title, body, data=None):
    print("🔥 send_push_notification called")
    print("Token:", token)
    print("Title:", title)

    try:
        message = messaging.Message(
            notification=messaging.Notification(
                title=title,
                body=body,
            ),
            token=token,
            data=data or {},
        )

        response = messaging.send(message)
        print("✅ Notification sent:", response)
        return response

    except Exception as e:
        print("❌ Firebase Error:", e)
        return None













        


# import os
# import json
# import firebase_admin
# from firebase_admin import credentials, messaging

# if not firebase_admin._apps:
#     try:
#         firebase_json = os.getenv("FIREBASE_SERVICE_ACCOUNT")

#         if firebase_json:
#             # Render / production
#             cred = credentials.Certificate(json.loads(firebase_json))
#         else:
#             # Local development
#             cred = credentials.Certificate("firebase-service-account.json")

#         firebase_admin.initialize_app(cred)
#         print("🔥 Firebase initialized successfully")

#     except Exception as e:
#         print("❌ Firebase initialization error:", e)
#         print("❌ FIREBASE_SERVICE_ACCOUNT environment variable missing")
# def send_push_notification(token, title, body, data=None):
#     print("🔥 send_push_notification called")
#     print("Token:", token)
#     print("Title:", title)

#     try:
#         message = messaging.Message(
#             notification=messaging.Notification(
#                 title=title,
#                 body=body,
#             ),
#             token=token,
#             data=data or {},
#         )

#         response = messaging.send(message)
#         print("✅ Notification sent:", response)
#         return response

#     except Exception as e:
#         print("❌ Firebase Error:", e)
#         return None