"""System URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from RMS import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('createPro/', views.createpro, name='createPro'),
    path('createemp/', views.createemp, name='createEmp'),
    path('createdep/', views.createdep, name='createdep'),
    path('viewProList/', views.viewProList, name='viewProList'),
    path('viewEmpList/', views.viewEmpList, name='viewEmpList'),
    path('viewTransactionList/', views.viewTransactionList, name='viewTransactionList'),
    path('empPro/', views.emppro, name='empPro'),
    path('home/', views.Base, name='base'),
    path('base/', views.Base, name='base'),

    path('signup/', views.signup, name ='signup'),
    path('signin/', views.signin, name = 'login'),
    path('signout/', views.signout, name = 'logout'),

]
