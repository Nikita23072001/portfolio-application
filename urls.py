from django import urls
from django.urls import path
from .portfolio import views  # Assuming "portfolio" directory is at the same level


urlpatterns = [
    path('', views.portfolio, name='portfolio'),
]
