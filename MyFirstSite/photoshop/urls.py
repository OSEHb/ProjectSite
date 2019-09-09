from django.urls import path
from . import views

urlpatterns = [
    path('', views.illustrations, name='illustrations_url'),
]
