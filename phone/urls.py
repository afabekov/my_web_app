from django.urls import path
from .views import phone

urlpatterns = [
    path('index/', phone, name='name')
]
