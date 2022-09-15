# from django.urls import path
from django.urls import re_path
from . import views

urlpatterns = [
    
    # path('',views.getData),
    re_path(r'^soap_service/', views.my_soap_application),

    
]