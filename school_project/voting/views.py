from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.utils import timezone
from .models import Vote, VoteOption, UserVote


class VotingListView(ListView):
    model = Vote
    context_object_name = 'Votes'
    template_name = 'voting/voting_list.html'


class VotingDetailView(DetailView):
    model = Vote
    template_name = 'voting/voting_detail.html'
    context_object_name = 'Vote'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        vote = self.object

        options = vote.voteoption_set.all()
        total_votes = UserVote.objects.filter(vote=vote).count()

        user_voted_option = None
        if self.request.user.is_authenticated:
            user_vote = UserVote.objects.filter(vote=vote, user=self.request.user).first()
            if user_vote:
                user_voted_option = user_vote.option

        context['options'] = options
        context['total_votes'] = total_votes
        context['user_voted_option'] = user_voted_option
        return context


class VoteSubmitView(LoginRequiredMixin, View):

    def post(self, request, pk):
        vote = get_object_or_404(Vote, pk=pk)

        if vote.end_date < timezone.now():
            messages.error(request, "Это голосование уже завершено.")
            return redirect('voting:voting-detail', pk=pk)

        if UserVote.objects.filter(vote=vote, user=request.user).exists():
            messages.warning(request, "Вы уже проголосовали в этом опросе.")
            return redirect('voting:voting-detail', pk=pk)

        option_id = request.POST.get('option')
        if not option_id:
            messages.error(request, "Вы не выбрали ни один вариант.")
            return redirect('voting:voting-detail', pk=pk)

        option = get_object_or_404(VoteOption, id=option_id, vote=vote)

        UserVote.objects.create(
            vote=vote,
            user=request.user,
            option=option,
            voted_at=timezone.now()
        )

        messages.success(request, "Ваш голос успешно учитан!")
        return redirect('voting:voting-detail', pk=pk)

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
