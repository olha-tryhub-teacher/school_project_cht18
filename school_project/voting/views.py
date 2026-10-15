from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, View, UpdateView, DeleteView
from .models import *
from django.urls import reverse_lazy
# Create your views here.


class VotingListView(ListView):
    model = Vote
    context_object_name = 'Votes'
    template_name = 'voting/voting_list.html'

class VotingDetailView(DetailView):
    model = Vote
    template_name = 'voting/voting_detail.html'
    context_object_name = 'Vote'

class VotingCreateView(CreateView):
    model = Vote
    form_class = Vote
    template_name = 'voting/voting_create.html'
    success_url = reverse_lazy('tasks:task-list')

class VotingUpdateView(UpdateView):
    model = Vote
    form_class = Vote
    template_name = 'voting/voting_update.html'
    success_url = reverse_lazy('tasks:task-list')

class VotingDeleteView(DeleteView):
    model = Vote
    template_name = 'voting/voting_delete.html'
    success_url = reverse_lazy('tasks:task-list')
