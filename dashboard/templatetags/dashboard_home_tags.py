from django import template
from django.contrib.auth import get_user_model

register = template.Library()

User = get_user_model()


@register.simple_tag()
def home_counters():
    total_users = User.objects.count()
    return {
        'total_users': total_users
    }
