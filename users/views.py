from allauth.account.views import SignupView, LoginView, LogoutView, PasswordChangeView, PasswordResetView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.

# class LoggedUserProfile()

@login_required
def logged_user_profile(request):
    # user = request.user
    # data = {
    #     'user': request.user
    # }
    return render(request, 'users/profile.html')


class AccountSignup(SignupView):
    template_name = 'users/signup.html'


class AccountLogin(LoginView):
    template_name = 'users/login.html'


class AccountLogout(LogoutView):
    pass


class AccountPasswordChange(PasswordChangeView):
    template_name = 'users/password_change.html'


class AccountPasswordReset(PasswordResetView):
    template_name = 'users/password_reset.html'
