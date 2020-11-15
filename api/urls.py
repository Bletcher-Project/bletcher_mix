from django.urls import path
from api import views

urlpatterns = [
    path('',views.index_page),
    path('synthesizing', views.bletcher_mix),
]