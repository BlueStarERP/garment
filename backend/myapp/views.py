from django.shortcuts import render
from django.http import JsonResponse
from django.core.paginator import Paginator

from .models import *

# Create your views here.
def landingpage(request):
    return render(request, 'index.html')


#HR
def hrdashboard(request):
    pass

def employeelist(request):
    emp = employee_profile.objects.all()
    paginator = Paginator(emp, 20)  # Show 20 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    context = {'emp':emp, 'page_obj':page_obj}
    return render(request, 'employee.html', context)

def employeeview(request):
    emp = employee_profile.objects.all()
    
    return JsonResponse({'message':'Success'})