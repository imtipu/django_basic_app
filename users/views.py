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
