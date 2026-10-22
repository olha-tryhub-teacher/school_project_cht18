from django.urls import path
from .views import PollListView, PollDetailView, VoteView

app_name = "polls"

urlpatterns = [
    path("", PollListView.as_view(), name="list"),
    path("<int:pk>/", PollDetailView.as_view(), name="detail"),
    path("<int:pk>/vote/", VoteView.as_view(), name="vote"), # Змінено тут
]