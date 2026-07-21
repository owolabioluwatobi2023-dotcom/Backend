from django.urls import path

from .views import (
    SaveDeviceTokenView,
    NotificationListView,
    LoginHistoryView,
    MarkNotificationReadView,
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
        "mark-read/",
        MarkNotificationReadView.as_view()
    ),


    path(
        "login-history/",
        LoginHistoryView.as_view()
    ),

]