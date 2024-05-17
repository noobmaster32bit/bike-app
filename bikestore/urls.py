"""
URL configuration for bikestore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from BikeKart import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',views.SignUpView.as_view(),name="signup"),
    path('signin/',views.SignInView.as_view(),name="signin"),
    path('index/',views.VehicleListView.as_view(),name="bikes-all"),
    path('bikes/add/',views.VehicleAddView.as_view(),name="bikes-add"),
    path('bikes/<int:pk>/',views.VehicleDetailView.as_view(),name="bikes-detail"),
    path('home/',views.HomeView.as_view(),name="home"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
