from rest_framework import serializers
from .models import Notification, LoginHistory


class NotificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notification
        fields = "__all__"



class LoginHistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = LoginHistory
        fields = "__all__"