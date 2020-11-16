from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.

@login_required(login_url='/accounts/login')
def dashboard_home(request):
    data = {
        'title': 'Dashboard'
    }
    return render(request, 'dashboard/index.html', data)
