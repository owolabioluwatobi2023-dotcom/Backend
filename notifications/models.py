# from django.db import models

# # Create your models here.
# from django.db import models
# from django.contrib.auth.models import User


# class Notification(models.Model):

#     NOTIFICATION_TYPES = (
#         ("welcome", "Welcome"),
#         ("login", "Login"),
#         ("wallet", "Wallet"),
#         ("airtime", "Airtime"),
#         ("data", "Data"),
#         ("cable", "Cable TV"),
#         ("electricity", "Electricity"),
#         ("bonus", "Referral Bonus"),
#     )


#     user = models.ForeignKey(
#         User,
#         on_delete=models.CASCADE,
#         related_name="notifications"
#     )


#     notification_type = models.CharField(
#         max_length=50,
#         choices=NOTIFICATION_TYPES
#     )


#     title = models.CharField(
#         max_length=255
#     )


#     message = models.TextField()


#     is_read = models.BooleanField(
#         default=False
#     )


#     created_at = models.DateTimeField(
#         auto_now_add=True
#     )


#     def __str__(self):
#         return self.title



# class DeviceToken(models.Model):

#     user = models.ForeignKey(
#         User,
#         on_delete=models.CASCADE
#     )

#     token = models.CharField(
#         max_length=500,
#         unique=True
#     )

#     device_name = models.CharField(
#         max_length=255,
#         blank=True
#     )

#     platform = models.CharField(
#         max_length=50,
#         default="android"
#     )

#     app_version = models.CharField(
#         max_length=50,
#         blank=True
#     )

#     created_at = models.DateTimeField(
#         auto_now_add=True
#     )

#     updated_at = models.DateTimeField(
#         auto_now=True
#     )


#     def __str__(self):
#         return self.user.username



# class LoginHistory(models.Model):

#     user = models.ForeignKey(
#         User,
#         on_delete=models.CASCADE
#     )

#     device_name = models.CharField(
#         max_length=255
#     )

#     ip_address = models.GenericIPAddressField(
#         null=True,
#         blank=True
#     )

#     login_time = models.DateTimeField(
#         auto_now_add=True
#     )


#     def __str__(self):
#         return self.user.username



from django.db import models
# Create your models here.

from django.contrib.auth.models import User
class Notification(models.Model):
    
    NOTIFICATION_TYPES = (
        ("welcome", "Welcome"),
        ("login", "Login"),
        ("wallet", "Wallet"),
        ("airtime", "Airtime"),
        ("data", "Data"),
        ("cable", "Cable TV"),
        ("electricity", "Electricity"),
        ("bonus", "Referral Bonus"),
        ("update", "Update"),
    )


    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="notifications"
    )


    notification_type = models.CharField(
        max_length=50,
        choices=NOTIFICATION_TYPES
    )


    title = models.CharField(
        max_length=255
    )


    # Normal text notification
    message = models.TextField()


    # HTML styled notification
    html_message = models.TextField(
        blank=True,
        null=True
    )


    is_read = models.BooleanField(
        default=False
    )


    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):
        return self.title

# class Notification(models.Model):

#     NOTIFICATION_TYPES = (
#         ("welcome", "Welcome"),
#         ("login", "Login"),
#         ("wallet", "Wallet"),
#         ("airtime", "Airtime"),
#         ("data", "Data"),
#         ("cable", "Cable TV"),
#         ("electricity", "Electricity"),
#         ("bonus", "Referral Bonus"),
#     )


#     user = models.ForeignKey(
#         User,
#         on_delete=models.CASCADE,
#         related_name="notifications"
#     )


#     notification_type = models.CharField(
#         max_length=50,
#         choices=NOTIFICATION_TYPES
#     )


#     title = models.CharField(
#         max_length=255
#     )


#     message = models.TextField()


#     is_read = models.BooleanField(
#         default=False
#     )


#     created_at = models.DateTimeField(
#         auto_now_add=True
#     )


#     def __str__(self):
#         return self.title



class DeviceToken(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    token = models.CharField(
        max_length=500,
        unique=True
    )

    device_name = models.CharField(
        max_length=255,
        blank=True
    )

    platform = models.CharField(
        max_length=50,
        default="android"
    )

    app_version = models.CharField(
        max_length=50,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )


    def __str__(self):
        return self.user.username



class LoginHistory(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    device_name = models.CharField(
        max_length=255
    )

    ip_address = models.GenericIPAddressField(
        null=True,
        blank=True
    )

    login_time = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):
        return self.user.username