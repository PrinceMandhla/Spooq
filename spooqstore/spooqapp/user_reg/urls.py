from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.my_view, name='login_page'),
    path('success/', views.success_view, name='success_page'),  # Update this if you have a separate view for the success page
    path('',views.reg_view, name ='reg_Page')
]