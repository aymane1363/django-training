# pages/views.py
from django.views.generic import TemplateView

class HomePageView(TemplateView): 
    template_name = "pages/home.html"

class AboutPageView(TemplateView): # new 
    template_name = "pages/about.html"