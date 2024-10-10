from django.urls import path 
from .views import loginView
urlpatterns = [
    path('http://localhost:3000/login',loginView.as_view(),name="login")
]
