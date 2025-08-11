from django.contrib import admin
from django.urls import path, include
from accounts import views


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('verify/<str:email_token>/', views.activate_email, name='activate_mail'),
    path('logout/', views.logout_page, name='logout'),
]
