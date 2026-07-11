from django.contrib import admin

# Register your models here.


from .models import (
    Notification,
    DeviceToken,
    LoginHistory
)


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):

    list_display = [
        "id",
        "user",
        "notification_type",
        "title",
        "is_read",
        "created_at",
    ]

    list_filter = [
        "notification_type",
        "is_read",
        "created_at",
    ]

    search_fields = [
        "user__username",
        "title",
        "message",
    ]


@admin.register(DeviceToken)
class DeviceTokenAdmin(admin.ModelAdmin):

    list_display = [
        "id",
        "user",
        "device_name",
        "platform",
        "created_at",
    ]

    search_fields = [
        "user__username",
        "token",
    ]


@admin.register(LoginHistory)
class LoginHistoryAdmin(admin.ModelAdmin):

    list_display = [
        "id",
        "user",
        "device_name",
        "ip_address",
        "login_time",
    ]

    search_fields = [
        "user__username",
        "ip_address",
    ]