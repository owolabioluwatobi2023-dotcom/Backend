from django.contrib import admin

# Register your models here.
# class AdminWallet(models.Model):
#     balance = models.FloatField(default=0)
# from .models import Wallet, Transaction


# @admin.register(Wallet)
# class WalletAdmin(admin.ModelAdmin):
#     list_display = (
#         "id",
#         "user",
#         "balance",
#     )

#     search_fields = (
#         "user__username",
#     )


# @admin.register(Transaction)
# class TransactionAdmin(admin.ModelAdmin):
#     list_display = (
#         "id",
#         "user",
#         "reference",
#         "amount",
#         "status",
#         "created_at",
#     )

#     search_fields = (
#         "user__username",
#         "reference",
#     )

#     list_filter = (
#         "status",
#     )

#     ordering = (
#         "-id",
#     )


    