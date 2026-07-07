# from django.urls import path
# from django.http import HttpResponse
# from .views import (
# verify_payment,
# wallet_balance

# )
# urlpatterns = [
#     path('verify/', verify_payment, name='verify_payment'),
#     path('wallet/balance/', wallet_balance),
# ]




# from django.urls import path
# from django.http import HttpResponse
# from .views import (
# verify_payment,
# wallet_balance

# )
# urlpatterns = [
#     path('verify/', verify_payment, name='verify_payment'),
#     path('wallet/balance/', wallet_balance),
# ]




# from django.urls import path
# from django.http import HttpResponse
# from .views import (
# verify_payment,
# wallet_balance,
# buy_product,
# vtpass_webhook

# )
# urlpatterns = [
#     path('verify/', verify_payment, name='verify_payment'),
#     path('wallet/balance/', wallet_balance),
#     path("buy-product/", buy_product),
#     path( "vtpass-webhook/",vtpass_webhook,),
# ]
from django.urls import path

from .views import (
    verify_payment,
    wallet_balance,
    buy_product,
    vtpass_webhook,
)


urlpatterns = [
    # Verify Paystack payment
    path(
        "verify/",
        verify_payment,
        name="verify-payment",
    ),

    # Wallet balance
    path(
        "wallet/balance/",
        wallet_balance,
        name="wallet-balance",
    ),

    # Buy product (VTU, airtime, data, etc.)
    path(
        "buy-product/",
        buy_product,
        name="buy-product",
    ),

    # VTpass webhook callback
    path(
        "vtpass-webhook/",
        vtpass_webhook,
        name="vtpass-webhook",
    ),
]