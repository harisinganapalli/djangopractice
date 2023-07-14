from django.shortcuts import render
from .decorators import *

# Create your views here.

def homepage(request,*args,**kwargs):
    context={}
    return render (request,"homepage.html",context)

# @student_access_only
# def student_view(request,*args,**kwargs):
#     context={}
#     return render(request,"studentview.html",context)


@student_access_only()
def student_view(request, *args, **kwargs):
    context = {}
    return render(request, "studentview.html", context)
 
@teacher_access_only
def teacher_view(request,*args,**kwargs):
    context={}
    return render (request,'teacherview.html',context)

@principal_access_only
def principal_view(request,*args,**kwargs):
    context={}
    return render(request,"principalview.html",context)

def login_view(request):
    context={}
    return render(request,"loginview.html",context)
