from django import forms
from .models import Result

class UploadData(forms.ModelForm):
    class Meta:
        model = Result
        fields = "__all__"