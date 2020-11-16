from django.urls import path, include

from .views import *

urlpatterns = [
    path('', dashboard_home, name="dashboard_home"),
    path('users/', UserListView.as_view(), name='user_list')
]
