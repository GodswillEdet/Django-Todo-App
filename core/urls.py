from django.urls import path

from . import views

name_app = 'core'

urlpatterns = [
    path('', views.homepage, name='homepage'),
]