from django.shortcuts import render
from django.http import JsonResponse
from django.core.paginator import Paginator

from .models import *

# Create your views here.
def landingpage(request):
    return render(request, 'index.html')