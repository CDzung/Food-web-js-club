"""JapaneseFoodWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from home import views
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('info/', views.info, name='info'),
    path('', views.home, name='home'),
    path('profile/', views.UserEditProfileView.as_view(), name = 'profile'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name= 'login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(next_page= 'login'), name='logout'),
    url(r'^signup/$', views.signup, name='signup'),

]
