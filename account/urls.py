from django.urls import path
from . import views

app_name= 'account'
urlpatterns = [
    # viewsからindexを読み込んで、nameをindexに
    path('login', views.login, name='login'),
]