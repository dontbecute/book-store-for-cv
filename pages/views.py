from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from books.models import Books

class indexView(TemplateView):
    template_name = "index.html"