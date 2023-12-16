from django.shortcuts import render

from .models import *
from .form import *

# Create your views here.
def home(request):
    d={'name':'feby','age':22}
    return render(request,'base.html')
def index(request):
    return render(request,'index.html')
def form2(request):
    if request.method=="POST":
        d=empform(request.POST)
        if d.is_valid():
            d.save()
            return list_item(request)
    return render(request,'form1.html')


def list_item(request):
    p=employe.objects.all()
    return render(request,'list.html',{'d':p})

def form3(request):
    if request.method=='POST':

        id1=request.POST.get('id')
        name=request.POST.get('nm')
        des=request.POST.get('ds')
        salry=request.POST.get('s')
        sa=employe.objects.create(empid=id1,empname=name,designation=des,salary=salry)
        sa.save()
        return list_item(request)
    return render(request,'form2.html')
 
            
    
    
