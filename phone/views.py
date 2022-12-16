from django.shortcuts import render
from .models import Phone


def phone(request):
    phone = Phone.objects.all()
    data = {
        'phone': phone
    }
    return render(request, 'index.html', data)
