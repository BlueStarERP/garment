from django.shortcuts import render
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.views.generic import TemplateView, View, CreateView, DetailView,FormView
#rest_framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from .serializers import *
from .models import *

# Create your views here.
def landingpage(request):
    return render(request, 'index.html')

#API
class departmentList(APIView):
        def get(self, request, format=None):
            departments = department.objects.all()
            serializer = departmentSerializer(departments, many=True)
            return Response(serializer.data)
            # return JsonResponse(serializer.data)
    



# Template View 
class hrDashboard(TemplateView):
    template_name = 'hrdashboard.html'
    
class adddepartment(View):
    def get(self,request):
        dept = request.GET['department_name']
        department.objects.create(department_name=dept)
        return JsonResponse({'status':'success'})


