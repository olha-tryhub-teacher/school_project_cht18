from django.urls import path

from .views import (
    MaterialListView,
    MaterialDetailView,
    MaterialCreateView,
)

urlpatterns = [
    path("", MaterialListView.as_view(), name="material-list"),
    path("<int:pk>/", MaterialDetailView.as_view(), name="material-detail"),
    path("upload/", MaterialCreateView.as_view(), name="material-upload"),
]