from django.urls import path
from . import views

app_name = 'games'

urlpatterns = [
    path('', views.index, name='index'),
    path('details/<int:id>', views.details, name='details'),
    path('browse', views.browse, name='browse'),
]
