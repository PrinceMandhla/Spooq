from django.views.generic import TemplateView
from django.http import HttpResponse

# Create your views here.

class MembersView (TemplateView):
        template_name = 'memb.html'

       
