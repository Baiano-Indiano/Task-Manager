from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse

@login_required
def admin_logout(request):
    """
    View personalizada para logout do admin que redireciona para a página inicial.
    """
    logout(request)
    return redirect(reverse('tasks:task_list'))
