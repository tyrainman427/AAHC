from django.shortcuts import render
from employee.models import *

# Create your views here.
def home(request):
    employee = Employee.objects.all()
    context = {
    'employee':employee,
    }
    return render(request,'website/home.html',context)

def application(request):
    application = Employee.objects.all()
    context = {
    'application':application,
    }
    return render(request,'website/open_positions.html',context)

def application_detail(request,id):


    return render(request, 'webiste/application_detail.html')

def career(request):
    return render(request,'website/careers.html')

def adminrec(request):
    return render(request,'website/admin.html')

def apply(request):
    return render(request,'website/application_form.html')
