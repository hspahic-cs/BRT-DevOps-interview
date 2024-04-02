from django.urls import path
from . import views

urlpatterns = [
    path('', views.order_page, name='order_page'),
    path('orderhistory/', views.order_history, name='order_history'),
]
