from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'account'
urlpatterns = [
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.register_User, name='register'),

    
   
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='account/password_reset_confirm.html',success_url='/account/reset/done/'
    ), name='password_reset_confirm'),
    path(
    'reset/done/',
    auth_views.PasswordResetCompleteView.as_view(template_name='account/password_reset_complete.html'),
    name='password_reset_complete',
),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='account/password_reset.html',email_template_name='account/password_reset_email.html',subject_template_name='account/password_reset_subject.txt',success_url='/account/password_reset_done/'), 
     name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='account/password_reset_done.html'), name='password_reset_done'),
]
    

