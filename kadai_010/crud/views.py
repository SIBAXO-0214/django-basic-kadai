from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from .models import Product

class ProductDetailView(DetailView):
    model = Product
    template_name = "detail.html"
