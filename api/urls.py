from django.urls import path
from api import views

urlpatterns = [
    path('v1/users/signup', views.create_user),
    path('v1/users/signin', views.validated_user),

    path('v1/models/yarth', views.model_yarth),
]