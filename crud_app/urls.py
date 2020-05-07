"""crud_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from client import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.ClientList.as_view(), name='client_list'),
    path('detail/<int:pk>', views.ClientDetail.as_view(), name='client_detail'),
    path('update/<int:pk>', views.ClientUpdate.as_view(), name='client_update'),
    path('delete/<int:pk>', views.ClientDelete.as_view(), name='client_delete'),
    path('create/', views.ClientCreate.as_view(), name='client_create'),
    
]
