from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def members (request):
        template = loader.get_template('memb1.html')
        return HttpResponse(template.render)
