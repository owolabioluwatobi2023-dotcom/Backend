from django.urls import path
from django.http import HttpResponse
from .views import (
buy_product,
vtpass_webhook,
create_virtual_account,
wallet,
paystack_webhook

)
urlpatterns = [
    path("buy-product/", buy_product),
    path( "vtpass-webhook/",vtpass_webhook,),
    path("create-virtual/", create_virtual_account),
    path( "wallet/",wallet,),
     path( "paystack-webhook/",paystack_webhook,),
    
  
]

