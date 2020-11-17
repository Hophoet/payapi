
from django.urls import path
from . import views 

app_name = 'core'

urlpatterns = [
    path('', views.TestView.as_view(), name='test' ),
    path('transfert/', views.TransfertView.as_view(), name='transfert')
]