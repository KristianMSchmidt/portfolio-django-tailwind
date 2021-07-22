from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('<str:projectname>/', views.project_detail_view, name='project_details'),
]

