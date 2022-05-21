from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('view',views.view_profile),
    path('edit',views.edit_profile),
    path('delete',views.delete_profile),
    
]