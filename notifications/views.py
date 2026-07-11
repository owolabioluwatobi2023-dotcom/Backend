from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Notification, DeviceToken, LoginHistory

from .serializers import (
    NotificationSerializer,
    LoginHistorySerializer,
)

# Save Firebase Device Token

class SaveDeviceTokenView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def post(self, request):

        token = request.data.get("token")

        if not token:
            return Response(
                {
                    "error": "FCM token required"
                },
                status=400
            )


        DeviceToken.objects.update_or_create(

            token=token,

            defaults={

                "user": request.user,

                "device_name":
                request.data.get(
                    "device_name",
                    ""
                ),

                "platform":
                request.data.get(
                    "platform",
                    "android"
                )
            }
        )


        return Response(
            {
                "message":
                "Token saved successfully"
            }
        )



# Get Notifications

class NotificationListView(APIView):

    permission_classes = [
        IsAuthenticated
    ]


    def get(self, request):

        notifications = Notification.objects.filter(

            user=request.user

        ).order_by(
            "-created_at"
        )


        serializer = NotificationSerializer(

            notifications,

            many=True

        )


        return Response(
            serializer.data
        )



# Login History

class LoginHistoryView(APIView):

    permission_classes = [
        IsAuthenticated
    ]


    def get(self, request):

        history = LoginHistory.objects.filter(

            user=request.user

        ).order_by(
            "-login_time"
        )


        serializer = LoginHistorySerializer(

            history,

            many=True

        )


        return Response(
            serializer.data
        )