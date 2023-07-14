from django.shortcuts import render
from . models import Product
from django.http import HttpResponse
from django.template.loader import get_template

from xhtml2pdf import pisa

# Create your views here.

def show_products(request):
    products=Product.objects.all()

    return render(request,'show_pdf_info.html',{'products':products}) 

def pdf_report_create(request):
    products=Product.objects.all()
    template_path='pdf_report.html' 
    response=HttpResponse(content_type='application/pdf')
    response['Content-Disposition']= 'filename=" "'
# response['Content-Disposition']= 'attachment; filename="products_report.pdf"' ###attachment is used for direct download the pdf
   #products_report.pdf is used to when a download a pdf its will givw inbuilt name as products_report.pdf
    template = get_template(template_path)    #get_template is used to  given a name and return a template object 
 
    html = template.render({'products':products})

    #  used  for create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show 
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response