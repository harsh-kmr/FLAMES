from dataclasses import fields
from .models import couple
from django.views.generic import CreateView, DetailView, ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class home(CreateView):
    model = couple
    template_name = "home.html"
    fields = '__all__'

class result(DetailView):
    model = couple
    template_name = "results.html"

class peek(LoginRequiredMixin, ListView):
    model = couple
    template_name = "peek.html"
    context_object_name= "couples"

class about(TemplateView):
    template_name = "about.html"

