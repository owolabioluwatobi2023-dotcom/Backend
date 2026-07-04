from django.contrib import admin
from .models import Wallet, Transaction


@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = ("owner", "amount", "updated_at")


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "reference",
        "transaction_id",
        "user",
        "product_name",
        "phone",
        "amount",
        "status",
        "created_at",
    )

    search_fields = (
        "reference",
        "transaction_id",
        "phone",
    )

    list_filter = ("status",)

    ordering = ("-created_at",)