from msilib.schema import ListView
from django.views.generic import DetailView, CreateView
from .forms import MaterialForm


from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView

from school_project_cht18.school_project.materials.models import Material


# Create your views here.

class MaterialListView(ListView):
    model = Material
    template_name="materials/material_list.html"
    context_object_name="materials"

class MaterialDetailView(DetailView):
    model = Material
    template_name = "materials/material_detail.html"
    context_object_name = "material"




class MaterialCreateView(CreateView):
    model = Material
    form_class = MaterialForm
    template_name = "materials/material_form.html"
    success_url = reverse_lazy("material-list")

    def form_valid(self, form):
        form.instance.uploaded_by = self.request.user
        return super().form_valid(form)