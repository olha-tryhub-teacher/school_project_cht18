from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.contrib import messages

from .models import Poll, Choice, Vote


class PollListView(ListView):
    model = Poll
    template_name = "polls/poll_list.html"
    context_object_name = "polls"
    paginate_by = 10


class PollDetailView(DetailView):
    model = Poll
    template_name = "polls/poll_detail.html"
    context_object_name = "poll"


def vote(request, pk):
    poll = get_object_or_404(Poll, pk=pk)

    if request.method == "POST":
        choice_id = request.POST.get("choice")
        choice = get_object_or_404(
            Choice,
            pk=choice_id,
            poll=poll
        )

        Vote.objects.get_or_create(
            user=request.user,
            poll=poll,
            choice=choice
        )

        messages.success(request, "Ваш голос зараховано!")

    return redirect("polls:detail", pk=poll.pk)