from django.views.generic import ListView
from django.shortcuts import render
from django.http import HttpResponse
from .models import Member
# Create your views here.

class MembersView (ListView):
        model = Member
        template_name = 'memb.html'
        context_object_name = 'members'



       
