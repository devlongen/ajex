from django.urls import path
from api import views

urlpatterns = [
    path('', views.post_user_data),
]