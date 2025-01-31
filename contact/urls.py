from . import views
from django.urls import path


app_name = 'contact'
urlpatterns = [
    path('info_plantillas/', views.info_plantillas, name="info_plantillas"),
    path('contact/', views.contact, name="contact"),
    path('info_plantillas/', views.info_plantillas, name="info_plantillas")

]
