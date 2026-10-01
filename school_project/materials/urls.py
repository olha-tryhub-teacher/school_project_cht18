from django.contrib import admin
from django.urls import path


from school_project_cht18.school_project.materials.views import (
    MaterialListView,
    MaterialDetailView,
    MaterialCreateView,
)



urlpatterns = [
    path("admin/", admin.site.urls),

    path("", MaterialListView.as_view(), name="material-list"),
    path("<int:pk>/", MaterialDetailView.as_view(), name="material-detail"),
    path("upload/", MaterialCreateView.as_view(), name="material-upload"),
]