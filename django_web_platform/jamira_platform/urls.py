from django.urls import path

from . import views

app_name = 'jamira_platform'
urlpatterns = [

    path('', views.home, name='home'),
    path('form/', views.model_form_upload, name='model_form_upload'),
]
