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
vtpass_webhook,
buy_airtime,
buy_data,
buy_cable


)
urlpatterns = [
    path('verify/', verify_payment, name='verify_payment'),
    path('wallet/balance/', wallet_balance),
    path( "vtpass-webhook/",vtpass_webhook,),
    path( "buy-airtime/",buy_airtime,),
    path( "buy-data/",buy_data,),
    path( "buy-cable/",buy_cable,),
]

