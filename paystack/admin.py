from django.contrib import admin
from .models import Wallet, Transaction


@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = ("owner", "amount", "updated_at")
    search_fields = ("owner__username",)
    ordering = ("-updated_at",)


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "user",
        "product_name",
        "phone",
        "amount",
        "status",
        "request_id",
        "transaction_id",
        "created_at",
    )

    search_fields = (
        "request_id",        # VTpass main ID
        "transaction_id",    # VTpass provider ID
        "reference",         # Paystack
        "phone",
        "user__username",
    )

    list_filter = (
        "status",
        "product_name",
    )

    ordering = ("-created_at",)

    readonly_fields = (
        "created_at",
        "updated_at",
        "request_id",
        "transaction_id",
    )