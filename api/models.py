from decimal import Decimal
from datetime import timedelta

from django.conf import settings
from django.db import models
from django.utils import timezone


# ==========================================
# LOGIN DEVICE
# ==========================================

class LoginDevice(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="login_devices"
    )

    user_agent = models.TextField()

    ip_address = models.GenericIPAddressField()

    last_login = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.user.username} - {self.ip_address}"


# ==========================================
# PASSWORD RESET OTP
# ==========================================

class PasswordResetOTP(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    otp = models.CharField(
        max_length=6
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    verified = models.BooleanField(
        default=False
    )

    def is_expired(self):
        return timezone.now() > (
            self.created_at + timedelta(minutes=10)
        )

    def __str__(self):
        return f"{self.user.username} - {self.otp}"

