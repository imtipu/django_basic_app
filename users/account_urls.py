from django.urls import path, include

from .views import *

urlpatterns = [
    path('profile/', logged_user_profile),
    path('signup/', AccountSignup.as_view(), name='account_signup'),
    path('login/', AccountLogin.as_view(), name='account_login'),
    path('logout/', AccountLogout.as_view(), name='account_logout'),
    path('password/change/', AccountPasswordChange.as_view(), name='account_change_password'),
]
