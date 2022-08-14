from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('<str:nav_id>/', views.home_view, name='home'),
]
