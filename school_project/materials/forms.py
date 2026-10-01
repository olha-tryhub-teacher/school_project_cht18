from django import forms
from .models import Material


class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = [
            "title",
            "description",
            "file",
            "link",
            "youtube_url",
            "material_type",
        ]