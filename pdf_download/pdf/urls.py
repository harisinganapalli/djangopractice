
from django.urls import path 
from . import views


urlpatterns=[
    path('s',views.show_products,name='show_pdf_products'),
    path('pdf_report',views.pdf_report_create,name='pdf_report')
]