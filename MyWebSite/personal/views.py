from django.shortcuts import render
from .models import Page

def page(request, name):
    page = Page.objects.get(name=name)
    return render(request, 'personal/page.html', {'body': page.body})

