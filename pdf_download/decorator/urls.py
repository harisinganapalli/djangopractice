from django.urls import path
from . import views as decorator_views
from django.contrib.auth.views import LoginView


app_name='decorator.urls'

urlpatterns=[
    path("home/", decorator_views.homepage,name="home_page"),
    path("student/",decorator_views.student_view,name="student"),
    path("teacher/",decorator_views.teacher_view,name="teacher"),
    path("principal/",decorator_views.principal_view,name="principal"),
    path("login/",decorator_views.login_view,name="login")

]