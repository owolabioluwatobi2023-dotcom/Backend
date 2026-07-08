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




from django.urls import path
from django.http import HttpResponse
from .views import (
verify_payment,
wallet_balance,
buy_product,
vtpass_webhook

)
urlpatterns = [
    path('verify/', verify_payment, name='verify_payment'),
    path('wallet/balance/', wallet_balance),
    path("buy-product/", buy_product),
    path( "vtpass-webhook/",vtpass_webhook,),
  
]

