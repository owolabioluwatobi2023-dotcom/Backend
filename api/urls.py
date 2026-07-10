# from django.urls import path
# from django.http import HttpResponse
# from .views import (

#     # AUTH
#     register_user,
#     user_profile,
#     login_user,
#     logout_user,
#     forgot_password,
#     reset_password,
#     google_login,

#     # PAYSTACK
#     initialize_payment,
#     paystack_balance,

#     # VTU CORE (CURRENT CLEAN VERSION)
#     buy_airtime,
#     buy_data,
#     buy_gotv,
#     buy_startimes,
#     verify_meter,
#     buy_electricity,
#     waec_variations,
#     buy_waec_registration,
#     requery_transaction,
#     waec_result_variations,
#     buy_waec_result_pin,
#     waec_result_requery,
#     jamb_variations,
#     jamb_requery,
#     buy_jamb_pin,
#     service_variations,
#     buy_showmax,
    
    
    
    
    

# )

# urlpatterns = [

#     # AUTH
#     path('register/', register_user),
#     path('login/', login_user),
#     path('user/', user_profile),
#     path('logout/', logout_user),
#     path('forgot-password/', forgot_password),
#     path('reset-password/', reset_password),
#     path('google-login/', google_login),

#     # PAYSTACK
#     path('paystack/initialize/', initialize_payment),
#     path('paystack/balance/', paystack_balance),

#     # TEST
#     path('test/', lambda request: HttpResponse("API IS WORKING")),

#     # AIRTIME & DATA
#     path('buy-airtime/', buy_airtime),
#     path('buy-data/', buy_data),

#     # TV
#     path('gotv/buy/', buy_gotv),
#     path('startimes/buy/', buy_startimes),

#     # ELECTRICITY
#     path('electricity/verify/', verify_meter),
#     path('electricity/pay/', buy_electricity),


#     # Education

#     path('waec-variations/', waec_variations),
#     path('buy-waec-registration', buy_waec_registration),

#     path('requery-transaction/', requery_transaction),



#     # resulchecker


#     path('waec-result-variations/', waec_result_variations),
#     path('buy-waec_result-pin', buy_waec_result_pin),

#     path('waec-result-requery/', waec_result_requery),



    
#     path('jamb-variations/', jamb_variations),
#     path('jamb-requery', jamb_requery),

#     path('buy-jamb-pin/', buy_jamb_pin),

#     path('service-variations/', service_variations, name='service-variations'),
#     path(" buy-showmax/", buy_showmax ),
  

# ]






from django.urls import path
from django.http import HttpResponse
from .views import app_stats

from .views import (

    # AUTH
    register_user,
    user_profile,
    login_user,
    logout_user,
    forgot_password,
    reset_password,
    google_login,

    # PAYSTACK
    initialize_payment,
    paystack_balance,
    service_variations,
    app_stats
   
   
    
    
    
    
    

)

urlpatterns = [

    # AUTH
    path('register/', register_user),
    path('login/', login_user),
    path('user/', user_profile),
    path('logout/', logout_user),
    path('forgot-password/', forgot_password),
    path('reset-password/', reset_password),
    path('google-login/', google_login),

    # PAYSTACK
    path('paystack/initialize/', initialize_payment),
    path('paystack/balance/', paystack_balance),

    # TEST
    path('test/', lambda request: HttpResponse("API IS WORKING")),

    # AIRTIME & DATA
    

    

    path('service-variations/', service_variations, name='service-variations'),
    path("app-stats/", app_stats, name="app_stats"),
       

  

]



