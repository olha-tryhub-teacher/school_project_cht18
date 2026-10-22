from django.urls import path
from .views import *

app_name = 'voting'

urlpatterns = [
    path('', VotingListView.as_view(), name='voting-list'),
    path('create/', VotingCreateView.as_view(), name='voting-create'),
    path('<int:pk>/', VotingDetailView.as_view(), name='voting-detail'),
    path('<int:pk>/vote/', VoteSubmitView.as_view(), name='voting-submit'),  # Новый маршрут
    path('<int:pk>/update/', VotingUpdateView.as_view(), name='voting-update'),
    path('<int:pk>/delete/', VotingDeleteView.as_view(), name='voting-delete'),
]