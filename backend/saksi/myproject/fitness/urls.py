from django.urls import path
from . import views

urlpatterns = [
    path('welcome/', views.welcome, name='welcome'),
    path('register/', views.signup, name='register'),
    path('login/', views.user_login, name='user_login'),
]