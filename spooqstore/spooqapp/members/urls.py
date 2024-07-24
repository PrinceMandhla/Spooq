from django.urls import path
from django.views.generic import TemplateView
from .views import MembersView

urlpatterns = [
    path('',MembersView.as_view(), name='members')

    ]