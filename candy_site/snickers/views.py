# from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class SnickersHomePageView(TemplateView):
    template_name = "snickers-home.html"
    
class AboutUsView(TemplateView):
    template_name = "about.html"

class HomePageView(TemplateView):
    template_name = "home.html"