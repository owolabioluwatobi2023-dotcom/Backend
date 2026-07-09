from django.contrib import admin
from .models import Wallet, Transaction


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
        "show_variation",
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
        "reference",
        "variation__variation_code",
        "variation__name",
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


    fieldsets = (

        (
            "User Information",
            {
                "fields": (
                    "user",
                    "email",
                    "phone",
                )
            },
        ),


        (
            "Product Information",
            {
                "fields": (
                    "service",
                    "product_name",
                    "variation",
                )
            },
        ),


        (
            "Payment Information",
            {
                "fields": (
                    "amount",
                    "total_amount",
                    "profit",
                    "commission",
                    "initial_balance",
                    "final_balance",
                )
            },
        ),


        (
            "Transaction Status",
            {
                "fields": (
                    "status",
                    "response_code",
                    "response_description",
                )
            },
        ),


        (
            "VTpass Information",
            {
                "fields": (
                    "transaction_id",
                    "request_id",
                    "unique_element",
                    "purchased_code",
                    "wallet_credit_id",
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


    ordering = (
        "-created_at",
    )


    def show_variation(self, obj):
        if obj.variation:
            return obj.variation.name
        return "-"


    show_variation.short_description = "Variation"