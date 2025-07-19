from django.shortcuts import render

# Create your views here.
def landingpage(request):
    return render(request, 'index.html')


#HR
def hrdashboard(request):
    pass

def employeelist(request):
    return render(request, 'employee.html')