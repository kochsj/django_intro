# from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class FrostedFlakesView(TemplateView):
    template_name = "frosted-flakes-home.html"