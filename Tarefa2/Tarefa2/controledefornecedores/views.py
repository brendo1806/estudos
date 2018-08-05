from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Controle
from .forms import ControleForm
from django.urls import reverse_lazy

class ControleListView(ListView):
    def get_context_object_name(self, object_list):
        return 'controle_list'
    def get_template_names(self):
        return 'controle_list.html'
    def get_queryset(self):
        return Controle.objects.all()

class ControleCreateView(CreateView):
    model = Controle
    def get_template_names(self):
        return'controle_form.html'
    def get_success_url(self):
        return reverse_lazy('controle:list')
    def get_form_class(self):
        return ControleForm

class ControleUpdateView(UpdateView):
    model = Controle
    def get_template_names(self):
        return'controle_form.html'
    def get_success_url(self):
        return reverse_lazy('controle:list')
    def get_form_class(self):
        return ControleForm


class ControleDetailView(DetailView):
    model = Controle
    def get_template_names(self):
        return 'controle_detail.html'

class ControleDeleteView(DeleteView):
    model = Controle
    def get_template_names(self):
        return 'controle_confim_delete.html'
    def get_success_url(self):
        return reverse_lazy('controle:list')

