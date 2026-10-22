from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from grades import models
from django.views.generic import ListView, DetailView, CreateView, View, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.core.exceptions import PermissionDenied


class GradeListView(ListView):
    model = models.Grade
    context_object_name = "grades"
    template_name = "grades/grade_list.html"
# Create your views here.
