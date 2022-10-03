from django.shortcuts import render

def index(request):
    """A View to return index page"""
    return render(request, 'home/index.html')

from django.http import JsonResponse
from .models import EmployeeData
# Create your views here.
def home(request):
   data=list(EmployeeData.objects.values())
   return JsonResponse(data,safe=False)