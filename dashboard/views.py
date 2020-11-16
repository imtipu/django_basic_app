from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, View, TemplateView

User = get_user_model()


class SuperUserLoginRequiredMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


@login_required(login_url='/accounts/login')
def dashboard_home(request):
    data = {
        'title': 'Dashboard'
    }
    return render(request, 'dashboard/index.html', data)


class UserListView(SuperUserLoginRequiredMixin, ListView):
    template_name = 'dashboard/user_list.html'
    context_object_name = 'users'
    model = User

# class TestView(TemplateView):
#     def get(self, request, *args, **kwargs):
#
