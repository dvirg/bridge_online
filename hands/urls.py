from django.urls import path
from . import views

app_name = 'hands'

urlpatterns = [
        path('', views.bridge_hand, name='index'),
]