from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    produtos = Produto.objects.all()

    return render(request, 'home.html', {'produtos': produtos})