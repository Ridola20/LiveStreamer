from django.urls import path
from . import views

urlpatterns = [
    path('Decoder-Reciever/', views.decoder_view, name="decoder")
]
