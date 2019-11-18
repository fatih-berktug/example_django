from django.shortcuts import render
from django.http import HttpResponse
from pyreportjasper2 import JasperPy
import os



def index(request):
    return render(request, 'index.html')


def generate(request):
    filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'files', 'hello_world.jrxml')
    name = 'hello_world.pdf'
    try:
        if not os.path.isfile(filename):
            raise ValueError("Filename doesn't exist")
        else:
            output = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'output')
            jasper = JasperPy()
            jasper.process(
                filename, output_file=output, format_list=["pdf"])
            pdf_generate = os.path.join(output, name)
            with open(pdf_generate, 'rb') as pdf:
                response = HttpResponse(pdf.read(), content_type='application/pdf')
                response['Content-Disposition'] = 'inline;filename='+name
                return response
            pdf.closed
    except ValueError as e:
        HttpResponse(e.message)
    return render(request, 'main/index.html')
