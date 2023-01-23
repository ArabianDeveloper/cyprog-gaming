from django.urls import path
from . import views

app_name = 'streams'

urlpatterns = [
    path('', views.streams, name='streams')
]
