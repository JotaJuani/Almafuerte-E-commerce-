from . import views
from django.urls import path


app_name = 'contact'
urlpatterns = [
    path('contact/', views.contact, name="contact"),
    path('contact_valid/', views.contact_valid, name="contact_valid"),
    path('contact_invalid/', views.contact_invalid, name="contact_invalid"),
    path('info_plantillas/', views.info_plantillas, name="info_plantillas")

]
