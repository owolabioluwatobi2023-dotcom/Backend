

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

from decimal import Decimal

from django.db import models
from django.conf import settings


# ==========================================
# WALLET
# ==========================================

class Wallet(models.Model):

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="wallet"
    )

    balance = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=Decimal("0.00")
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )


    def __str__(self):
        return f"{self.user.username} Wallet"


# ==========================================
# PAYSTACK VIRTUAL ACCOUNT
# ==========================================

class VirtualAccount(models.Model):

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="virtual_account"
    )

    customer_code = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    account_number = models.CharField(
        max_length=20,
        unique=True
    )

    account_name = models.CharField(
        max_length=200
    )

    bank_name = models.CharField(
        max_length=100
    )

    account_reference = models.CharField(
        max_length=100,
        unique=True,
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):
        return f"{self.account_name} - {self.account_number}"



# ==========================================
# WALLET TRANSACTIONS
# ==========================================

class WalletTransaction(models.Model):

    CREDIT = "credit"
    DEBIT = "debit"


    TYPE_CHOICES = [

        (CREDIT, "Credit"),

        (DEBIT, "Debit"),

    ]


    PENDING = "pending"
    SUCCESS = "success"
    FAILED = "failed"


    STATUS_CHOICES = [

        (PENDING, "Pending"),

        (SUCCESS, "Success"),

        (FAILED, "Failed"),

    ]


    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="wallet_transactions"
    )


    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )


    transaction_type = models.CharField(
        max_length=10,
        choices=TYPE_CHOICES
    )


    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=PENDING
    )


    reference = models.CharField(
        max_length=100,
        unique=True
    )


    description = models.CharField(
        max_length=255,
        blank=True
    )


    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):

        return (
            f"{self.user.username} "
            f"{self.transaction_type} "
            f"₦{self.amount}"
        )



# ==========================================
# DATA / AIRTIME VARIATIONS
# ==========================================

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



# ==========================================
# VTU TRANSACTION
# ==========================================

class Transaction(models.Model):

    STATUS_CHOICES = [

        ("pending", "Pending"),

        ("processing", "Processing"),

        ("delivered", "Delivered"),

        ("failed", "Failed"),

        ("reversed", "Reversed"),

    ]


    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="transactions"
    )


    reference = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        db_index=True
    )


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


    service = models.CharField(
        max_length=100,
        blank=True,
        default=""
    )


    product_name = models.CharField(
        max_length=255,
        blank=True,
        default=""
    )


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

        return f"{self.user.username} - {self.product_name}"