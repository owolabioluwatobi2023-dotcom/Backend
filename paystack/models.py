

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

#     # Paystack reference (can repeat in edge cases, so NOT unique)
#     reference = models.CharField(
#         max_length=100,
#         blank=True,
#         null=True,
#         db_index=True
#     )

#     # VTpass requestId (THIS is your real idempotency key)
#     request_id = models.CharField(
#         max_length=100,
#         unique=True,   # keep ONLY this unique
#         db_index=True
#     )

#     transaction_id = models.CharField(
#         max_length=100,
#         blank=True,
#         default=""
#     )

#     product_name = models.CharField(
#         max_length=200,
#         blank=True,
#         default=""
#     )

#     unique_element = models.CharField(
#         max_length=100,
#         blank=True,
#         default=""
#     )

#     phone = models.CharField(
#         max_length=20,
#         blank=True,
#         default=""
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
#         blank=True,
#         default=""
#     )

#     response_description = models.CharField(
#         max_length=255,
#         blank=True,
#         default=""
#     )

#     purchased_code = models.TextField(
#         blank=True,
#         default=""
#     )

#     wallet_credit_id = models.CharField(
#         max_length=100,
#         blank=True,
#         default=""
#     )

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

#     variation_code = models.CharField(
#         max_length=100,
#         unique=True
#     )

#     name = models.CharField(max_length=255)

#     amount = models.DecimalField(
#         max_digits=12,
#         decimal_places=2
#     )

#     fixed_price = models.BooleanField(default=True)
#     active = models.BooleanField(default=True)

#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)



# =========================
# WALLET
# =========================

# =========================
# WALLET
# =========================

from django.db import models
from django.contrib.auth.models import User


# =========================
# WALLET
# =========================

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

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.owner.username} - ₦{self.amount}"


# =========================
# DATA VARIATIONS
# =========================

class VariationCode(models.Model):

    service = models.CharField(
        max_length=100
    )

    variation_code = models.CharField(
        max_length=100,
        unique=True
    )

    name = models.CharField(
        max_length=255
    )

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    fixed_price = models.BooleanField(
        default=True
    )

    active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.service} - {self.name}"


# =========================
# TRANSACTION
# =========================

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


    # Paystack reference

    reference = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        db_index=True
    )


    # VTpass

    request_id = models.CharField(
        max_length=100,
        unique=True,
        blank=True,
        null=True,
        db_index=True
    )


    transaction_id = models.CharField(
        max_length=100,
        blank=True,
        default=""
    )


    # Service

    service = models.CharField(
        max_length=100,
        blank=True,
        default=""
    )


    # Product

    product_name = models.CharField(
        max_length=255,
        blank=True,
        default=""
    )


    # Link to variation

    variation = models.ForeignKey(
        VariationCode,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="transactions"
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


    unique_element = models.CharField(
        max_length=100,
        blank=True,
        default=""
    )


    # Amounts

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


    profit = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )


    commission = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )


    # Wallet snapshot

    initial_balance = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )


    final_balance = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )


    # VTpass response

    response_code = models.CharField(
        max_length=20,
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


    reversed = models.BooleanField(
        default=False
    )


    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default="pending",
        db_index=True
    )


    created_at = models.DateTimeField(
        auto_now_add=True
    )


    updated_at = models.DateTimeField(
        auto_now=True
    )


    def __str__(self):

        if self.variation:
            return f"{self.user.username} - {self.variation.name}"

        return f"{self.user.username} - {self.product_name}"






