from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView
from snacks.models import Snack

class SnackListView(ListView):
  template_name = 'snack_list.html'
  model = Snack
  context_object_name = 'snacks'

class SnackDetailView(DetailView):
  template_name = 'snack_detail.html'
  model = Snack
