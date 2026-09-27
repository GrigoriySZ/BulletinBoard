from django.urls import path
from . import views

app_name = 'userAccoutn'

urlpatterns = [
    path('', views.register, name='register'),
]
