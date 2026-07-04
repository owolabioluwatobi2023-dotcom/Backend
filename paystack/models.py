# from django.db import models
# from django.contrib.auth.models import User


# class Transaction(models.Model):
#     user = models.ForeignKey(
#         User,
#         on_delete=models.CASCADE
#     )

#     reference = models.CharField(
#         max_length=100,
#         unique=True
#     )

#     amount = models.DecimalField(
#         max_digits=12,
#         decimal_places=2
#     )

#     status = models.CharField(
#         max_length=20
#     )

#     email = models.EmailField(
#         blank=True,
#         null=True
#     )

#     created_at = models.DateTimeField(
#         auto_now_add=True
#     )

#     def __str__(self):
#         return self.reference


# class Wallet(models.Model):
#     owner = models.ForeignKey(
#         User,
#         on_delete=models.CASCADE
#     )

#     amount = models.DecimalField(
#         max_digits=12,
#         decimal_places=2,
#         default=0
#     )

#     def __str__(self):
#         return f"{self.owner.username} - {self.amount}"




# from django.db import models
# from django.contrib.auth.models import User


# class Transaction(models.Model):
#     user = models.ForeignKey(
#         User,
#         on_delete=models.CASCADE,
#         related_name="transactions"
#     )

#     reference = models.CharField(
#         max_length=100,
#         unique=True
#     )

#     amount = models.DecimalField(
#         max_digits=12,
#         decimal_places=2
#     )

#     status = models.CharField(
#         max_length=20
#     )

#     email = models.EmailField(
#         blank=True,
#         null=True
#     )

#     created_at = models.DateTimeField(
#         auto_now_add=True
#     )

#     def __str__(self):
#         return f"{self.user.username} - {self.reference}"


# class Wallet(models.Model):
#     owner = models.OneToOneField(
#         User,
#         on_delete=models.CASCADE,
#         related_name="wallet"
#     )

#     amount = models.DecimalField(
#         max_digits=12,
#         decimal_places=2,
#         default=0
#     )

#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return f"{self.owner.username} - ₦{self.amount}"







#         from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.contrib.auth.models import User
# from .models import Wallet


# @receiver(post_save, sender=User)
# def create_wallet(sender, instance, created, **kwargs):
#     if created:
#         Wallet.objects.create(owner=instance)


# @receiver(post_save, sender=User)
# def save_wallet(sender, instance, **kwargs):
#     Wallet.objects.get_or_create(owner=instance)







    


# from django.db import models
# from django.contrib.auth.models import User


# class Transaction(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="transactions")
#     reference = models.CharField(max_length=100, unique=True)
#     amount = models.DecimalField(max_digits=12, decimal_places=2)
#     status = models.CharField(max_length=20)
#     email = models.EmailField(blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.user.username} - {self.reference}"


# class Wallet(models.Model):
#     owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name="wallet")
#     amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return f"{self.owner.username} - ₦{self.amount}"
    





#     request_id = models.CharField(max_length=100, unique=True)
# transaction_id = models.CharField(max_length=100, blank=True)

# status = models.CharField(max_length=30)
# response_code = models.CharField(max_length=10, blank=True)
# response_description = models.CharField(max_length=255, blank=True)

# product_name = models.CharField(max_length=200, blank=True)
# phone = models.CharField(max_length=20, blank=True)
# email = models.EmailField(blank=True)
# unique_element = models.CharField(max_length=100, blank=True)

# amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
# total_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
# commission = models.DecimalField(max_digits=12, decimal_places=2, default=0)

# purchased_code = models.TextField(blank=True)

# wallet_credit_id = models.CharField(max_length=100, blank=True)

# reversed = models.BooleanField(default=False)


# from django.db import models


# class VariationCode(models.Model):
#     service_id = models.CharField(max_length=100)
#     variation_code = models.CharField(max_length=100, unique=True)
#     name = models.CharField(max_length=255)
#     amount = models.DecimalField(max_digits=12, decimal_places=2)
#     fixed_price = models.BooleanField(default=True)
#     active = models.BooleanField(default=True)

#     def __str__(self):
#         return self.name




# from django.db import models
# from django.contrib.auth.models import User


# class Wallet(models.Model):
#     user = models.OneToOneField(
#         User,
#         on_delete=models.CASCADE,
#         related_name="wallet"
#     )

#     balance = models.DecimalField(
#         max_digits=12,
#         decimal_places=2,
#         default=0
#     )

#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return f"{self.user.username} - ₦{self.balance}"


# class Transaction(models.Model):

#     STATUS_CHOICES = (
#         ("pending", "Pending"),
#         ("processing", "Processing"),
#         ("delivered", "Delivered"),
#         ("failed", "Failed"),
#         ("reversed", "Reversed"),
#     )

#     user = models.ForeignKey(
#         User,
#         on_delete=models.CASCADE,
#         related_name="transactions"
#     )

#     reference = models.CharField(
#         max_length=100,
#         unique=True,
#         blank=True,
#         null=True
#     )

#     request_id = models.CharField(
#         max_length=100,
#         unique=True
#     )

#     transaction_id = models.CharField(
#         max_length=100,
#         blank=True,
#         null=True
#     )

#     product_name = models.CharField(
#         max_length=200,
#         blank=True
#     )

#     unique_element = models.CharField(
#         max_length=100,
#         blank=True
#     )

#     phone = models.CharField(
#         max_length=20,
#         blank=True
#     )

#     email = models.EmailField(
#         blank=True,
#         null=True
#     )

#     amount = models.DecimalField(
#         max_digits=12,
#         decimal_places=2,
#         default=0
#     )

#     total_amount = models.DecimalField(
#         max_digits=12,
#         decimal_places=2,
#         default=0
#     )

#     commission = models.DecimalField(
#         max_digits=12,
#         decimal_places=2,
#         default=0
#     )

#     response_code = models.CharField(
#         max_length=10,
#         blank=True
#     )

#     response_description = models.CharField(
#         max_length=255,
#         blank=True
#     )

#     purchased_code = models.TextField(
#         blank=True
#     )

#     wallet_credit_id = models.CharField(
#         max_length=100,
#         blank=True
#     )

#     reversed = models.BooleanField(
#         default=False
#     )

#     status = models.CharField(
#         max_length=30,
#         choices=STATUS_CHOICES,
#         default="pending"
#     )

#     created_at = models.DateTimeField(
#         auto_now_add=True
#     )

#     updated_at = models.DateTimeField(
#         auto_now=True
#     )

#     def __str__(self):
#         return f"{self.request_id} - {self.status}"


# class VariationCode(models.Model):

#     service_id = models.CharField(
#         max_length=100
#     )

#     variation_code = models.CharField(
#         max_length=100,
#         unique=True
#     )

#     name = models.CharField(
#         max_length=255
#     )

#     amount = models.DecimalField(
#         max_digits=12,
#         decimal_places=2
#     )

#     fixed_price = models.BooleanField(
#         default=True
#     )

#     active = models.BooleanField(
#         default=True
#     )

#     created_at = models.DateTimeField(
#         auto_now_add=True
#     )

#     updated_at = models.DateTimeField(
#         auto_now=True
#     )

#     def __str__(self):
#         return f"{self.service_id} - {self.name}"

# import uuid
# from django.db import models
# from django.contrib.auth.models import User


# class Wallet(models.Model):
#     owner = models.OneToOneField(
#         User,
#         on_delete=models.CASCADE,
#         related_name="wallet"
#     )

#     amount = models.DecimalField(
#         max_digits=12,
#         decimal_places=2,
#         default=0
#     )

#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return f"{self.owner.username} - ₦{self.amount}"


# class Transaction(models.Model):

#     STATUS_CHOICES = (
#         ("pending", "Pending"),
#         ("processing", "Processing"),
#         ("delivered", "Delivered"),
#         ("failed", "Failed"),
#         ("reversed", "Reversed"),
#     )

#     user = models.ForeignKey(
#         User,
#         on_delete=models.CASCADE,
#         related_name="transactions"
#     )

#     reference = models.CharField(
#         max_length=100,
#         unique=True,
#         blank=True,
#         null=True
#     )

#     # ✅ FIX: use UUIDField instead of CharField
#     request_id = models.UUIDField(
#         default=uuid.uuid4,
#         unique=True,
#         editable=False
#     )

#     transaction_id = models.CharField(max_length=100, blank=True, default="")
#     product_name = models.CharField(max_length=200, blank=True, default="")
#     unique_element = models.CharField(max_length=100, blank=True, default="")
#     phone = models.CharField(max_length=20, blank=True, default="")

#     email = models.EmailField(blank=True, null=True)

#     amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
#     total_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
#     commission = models.DecimalField(max_digits=12, decimal_places=2, default=0)

#     response_code = models.CharField(max_length=10, blank=True, default="")
#     response_description = models.CharField(max_length=255, blank=True, default="")
#     purchased_code = models.TextField(blank=True, default="")

#     wallet_credit_id = models.CharField(max_length=100, blank=True, default="")
#     reversed = models.BooleanField(default=False)

#     status = models.CharField(
#         max_length=30,
#         choices=STATUS_CHOICES,
#         default="pending"
#     )

#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return f"{self.request_id} - {self.status}"


# class VariationCode(models.Model):
#     service_id = models.CharField(max_length=100)

#     variation_code = models.CharField(max_length=100, unique=True)
#     name = models.CharField(max_length=255)

#     amount = models.DecimalField(max_digits=12, decimal_places=2)

#     fixed_price = models.BooleanField(default=True)
#     active = models.BooleanField(default=True)

#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.name

from django.db import models
from django.contrib.auth.models import User


class Wallet(models.Model):
    owner = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="wallet"
    )

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    


class Transaction(models.Model):

    STATUS_CHOICES = (
        ("pending", "Pending"),
        ("processing", "Processing"),
        ("delivered", "Delivered"),
        ("failed", "Failed"),
        ("reversed", "Reversed"),
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="transactions"
    )

    reference = models.CharField(
        max_length=100,
        unique=True,
        blank=True,
        null=True
    )

    # VTpass requestId
    request_id = models.CharField(
        max_length=100,
        unique=True,
        db_index=True
    )

    transaction_id = models.CharField(
        max_length=100,
        blank=True,
        default=""
    )

    product_name = models.CharField(
        max_length=200,
        blank=True,
        default=""
    )

    unique_element = models.CharField(
        max_length=100,
        blank=True,
        default=""
    )

    phone = models.CharField(
        max_length=20,
        blank=True,
        default=""
    )

    email = models.EmailField(
        blank=True,
        null=True
    )

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    total_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    commission = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    response_code = models.CharField(
        max_length=10,
        blank=True,
        default=""
    )

    response_description = models.CharField(
        max_length=255,
        blank=True,
        default=""
    )

    purchased_code = models.TextField(
        blank=True,
        default=""
    )

    wallet_credit_id = models.CharField(
        max_length=100,
        blank=True,
        default=""
    )

    reversed = models.BooleanField(default=False)

    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default="pending"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.request_id} - {self.status}"


class VariationCode(models.Model):

    service_id = models.CharField(max_length=100)

    variation_code = models.CharField(
        max_length=100,
        unique=True
    )

    name = models.CharField(max_length=255)

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    fixed_price = models.BooleanField(default=True)
    active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

  