# from django.shortcuts import render

# Insert views here

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from .models import ClientModel

# Create your views here.


class ClientList(ListView):
    model = ClientModel
    template_name = 'client/client_list.html'


class ClientDetail(DetailView):
    model = ClientModel
    template_name = 'client/client_detail.html'


class ClientUpdate(UpdateView):
    model = ClientModel
    fields = '__all__'
    template_name = 'client/client_form.html'
    success_url = reverse_lazy('client_list')


class ClientDelete(DeleteView):
    model = ClientModel
    fields = '__all__'
    template_name = 'client/client_delete_confirm.html'
    success_url = reverse_lazy('client_list')


class ClientCreate(CreateView):
    model = ClientModel
    fields = '__all__'
    template_name = 'client/client_form.html'
    success_url = reverse_lazy('client_list')
