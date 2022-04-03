from django.urls import path
from . import views
urlpatterns=[
    path('',views.loadhome),
    path('FA',views.simple_upload,name='fileAction'),
]