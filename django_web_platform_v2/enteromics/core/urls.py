from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('forms/', views.upload, name='upload'),
    path('progress/', views.progress, name='progress'),
    path('forms2/', views.model_upload, name='model_upload'),
]
