from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from .models import CalendarDay

class CalendarListView(ListView):
    model = CalendarDay
    template_name = 'calendarapp/calendar_list.html'
    context_object_name = 'days'
    ordering = ['date']

class CalendarDetailView(DetailView):
    model = CalendarDay
    template_name = 'calendarapp/calendar_detail.html'
    context_object_name = 'day'
