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
        "product_name",
        "phone",
        "amount",
        "profit",
        "commission",
        "status",
        "created_at",
    )

    readonly_fields = (
        "request_id",
        "transaction_id",
        "created_at",
        "updated_at",
        "profit",
    )

    fieldsets = (
        (
            "Transaction Information",
            {
                "fields": (
                    "user",
                    "product_name",
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

        "service_id",

        "variation_code",

        "name",

        "amount",

        "active",

    )


    search_fields = (

        "service_id",

        "variation_code",

        "name",

    )


    list_filter = (

        "active",

        "fixed_price",

    )


    ordering = (

        "service_id",

        "amount",

    )