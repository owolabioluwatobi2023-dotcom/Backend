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
        "total_amount",
        "status",
        "created_at",
    )

    search_fields = (
        "user__username",
        "phone",
        "request_id",
        "transaction_id",
        "variation_name",
        "variation_code",
    )

    list_filter = (
        "service",
        "status",
        "created_at",
    )

    ordering = (
        "-created_at",
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

    fieldsets = (
        (
            "Transaction Information",
            {
                "fields": (
                    "user",
                    "service",
                    "product_name",
                    "variation_code",
                    "variation_name",
                    "phone",
                    "email",
                    "status",
                )
            },
        ),
        (
            "Money",
            {
                "fields": (
                    "amount",
                    "profit",
                    "commission",
                    "total_amount",
                    "initial_balance",
                    "final_balance",
                )
            },
        ),
        (
            "Identifiers",
            {
                "fields": (
                    "request_id",
                    "transaction_id",
                    "reference",
                )
            },
        ),
        (
            "VTpass Response",
            {
                "fields": (
                    "response_code",
                    "response_description",
                    "purchased_code",
                    "wallet_credit_id",
                    "unique_element",
                )
            },
        ),
        (
            "Dates",
            {
                "fields": (
                    "created_at",
                    "updated_at",
                )
            },
        ),
    )


# =========================
# VARIATION CODE ADMIN
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