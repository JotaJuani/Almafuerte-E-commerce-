from django.urls import path
from .import views
from . import webhooks

app_name = 'payment'
urlpatterns = [

    path('completed/', views.payment_completed, name='completed'),
    path('canceled/', views.payment_canceled, name='canceled'),
    path('pending/', views.payment_pending, name='pending'),
    path('webhook/', webhooks.stripe_webhook, name='stripe-webhook')


]
