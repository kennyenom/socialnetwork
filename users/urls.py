from django import forms


from django.urls import path
from .import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('signup',views.signup,name='blog-signup'),
    path('profile',views.profile,name='blog-profile'),
    path('login',auth_view.LoginView.as_view(template_name='users/login.html'),name='blog-login'),
    path('logout',auth_view.LogoutView.as_view(template_name='users/logout.html'),name='blog-logout'),
     path('password_reset/', auth_view.PasswordResetView.as_view(template_name='users/password_reset.html'),
         name='password_reset'),
    path('password_reset_done/', auth_view.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
         name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password_reset_complete/', auth_view.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),

]