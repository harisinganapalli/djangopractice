from functools import wraps
from django.contrib import messages 
from django.http import HttpResponse
from django .shortcuts import redirect
def student_test_function(user):
    if user.is_student:
        return True
    return False
    
def teacher_test_function(user):
    if user.is_teacher:
        return True 
    return False 

def principal_test_function(user):
    if user.is_principal:
        return True
    return False 


# def student_access_only():
#     def decorator(view):
#         @wraps(view)  #@wraps is a decorator that is applied to the wrapper function of a decorator.  wrapper function means used to modify or extend the behavior of an existing function
#         def _wrapped_view(request,*args,**kwargs):
#             if not student_test_function(request.user):
#                 return HttpResponse("youbare not a Student You not allowed to access this Page..!")
#             return view(request,*args,**kwargs)
#         return _wrapped_view
#     return decorator

def student_access_only():
    def decorator(view):
        @wraps(view)
        def _wrapped_view(request, *args, **kwargs):
            if not student_test_function(request.user):
                return HttpResponse("You are not a student and \
                        you are not allowed to access this page !")
            return view(request, *args, **kwargs)
        return _wrapped_view
    return decorator
 
def teacher_access_only(view_to_return="decorator_urls:home"):
    def decorator(view):
        def _wrapped_view(request,*args,**kwargs):
            if not teacher_test_function(request.user):
                messages.error(request,"You cant accesss the Teacher Page..!")
                return redirect(view_to_return)
            return view(request,*args,**kwargs)
        return _wrapped_view
    return decorator  


def principal_access_only(message_to_delivery="Not allowed to access the Principal Page ,Login as Principal..!"):
    def decorator(view):
        @wraps(view)
        def _wrapped_view(request,*args,**kwargs):
            if not principal_test_function(request.user):
                messages.error(request,message_to_delivery,)
                return redirect ("decorator_urls:login")
            return view(request,*args,**kwargs)
        return _wrapped_view
    return decorator

              