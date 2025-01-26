
from django.contrib import admin
from django.urls import path,include
from myapp import views
urlpatterns = [
        path("",views.index, name='home'),
        path("aboutpage",views.aboutpage,name='aboutpage'),
        path("contact",views.contact,name='contact'),
        path("monuments",views.monuments,name='monuments'),
        path("gallery",views.gallery,name='gallery'),
        
]
