from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, View, UpdateView, DeleteView
from .models import *
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
