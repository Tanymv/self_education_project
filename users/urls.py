from django.urls import path
from . import views

urlpatterns = [

    path('', views.landing, name='landing'),
    path('profiles/', views.profiles, name='profiles'),
    path('landing/', views.landingLogin, name='landingLogin'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),
]