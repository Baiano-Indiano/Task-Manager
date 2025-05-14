"""
URL configuration for taskmanager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView
from django.contrib.auth.decorators import login_required
from tasks.admin_auth import admin_logout
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView as DjangoLogoutView

# Sobrescrevendo a view de logout do admin
admin.site.logout = login_required(admin.site.logout)

urlpatterns = [
    # URL personalizada para logout do admin que redireciona para a página inicial
    path('admin/logout/', admin_logout, name='admin_logout'),
    path('admin/', admin.site.urls),
    # URLs de autenticação
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    # View personalizada para logout que aceita GET e POST
    path('accounts/logout/', DjangoLogoutView.as_view(
        template_name='registration/logout.html',
        next_page='login',
        http_method_names=['get', 'post', 'options']
    ), name='logout'),
    
    # URLs de redefinição de senha
    path('accounts/password_reset/', 
         auth_views.PasswordResetView.as_view(
             template_name='registration/password_reset_form.html',
             email_template_name='registration/password_reset_email.html',
             subject_template_name='registration/password_reset_subject.txt'
         ), 
         name='password_reset'),
    path('accounts/password_reset/done/', 
         auth_views.PasswordResetDoneView.as_view(
             template_name='registration/password_reset_done.html'
         ), 
         name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', 
         auth_views.PasswordResetConfirmView.as_view(
             template_name='registration/password_reset_confirm.html'
         ), 
         name='password_reset_confirm'),
    path('accounts/reset/done/', 
         auth_views.PasswordResetCompleteView.as_view(
             template_name='registration/password_reset_complete.html'
         ), 
         name='password_reset_complete'),
    
    # URLs do aplicativo
    path('', include('tasks.urls')),
]
