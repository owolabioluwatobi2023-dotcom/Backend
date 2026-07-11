from django.urls import path

from .views import (
    SaveDeviceTokenView,
    NotificationListView,
    LoginHistoryView
)

urlpatterns = [

    path(
        "save-token/",
        SaveDeviceTokenView.as_view()
    ),

    path(
        "list/",
        NotificationListView.as_view()
    ),

    path(
        "login-history/",
        LoginHistoryView.as_view()
    ),

]