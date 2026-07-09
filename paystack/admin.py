from django.contrib import admin
from .models import Wallet, Transaction, VariationCode


# =========================
# WALLET ADMIN
# =========================

@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):

    list_display = (
        "owner",
        "amount",
        "created_at",
        "updated_at",
    )

    search_fields = (
        "owner__username",
        "owner__email",
    )

    ordering = (
        "-updated_at",
    )



# =========================
# TRANSACTION ADMIN
# =========================

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "user",
        "service",
        "product_name",
        "variation_name",
        "phone",
        "amount",
        "profit",
        "commission",
        "status",
        "created_at",
    )


    search_fields = (
        "user__username",
        "user__email",
        "phone",
        "request_id",
        "transaction_id",
        "variation_code",
        "variation_name",
    )


    list_filter = (
        "service",
        "status",
        "created_at",
    )


    readonly_fields = (
        "request_id",
        "transaction_id",
        "reference",
        "profit",
        "commission",
        "initial_balance",
        "final_balance",
        "created_at",
        "updated_at",
    )


    ordering = (
        "-created_at",
    )



# =========================
# VARIATION ADMIN
# =========================

@admin.register(VariationCode)
class VariationCodeAdmin(admin.ModelAdmin):

    list_display = (
        "service",
        "variation_code",
        "name",
        "amount",
        "fixed_price",
        "active",
        "created_at",
    )


    search_fields = (
        "service",
        "variation_code",
        "name",
    )


    list_filter = (
        "service",
        "active",
        "fixed_price",
    )


    ordering = (
        "service",
        "amount",
    )