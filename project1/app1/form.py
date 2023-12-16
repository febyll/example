from django import forms
from .models import *

class empform(forms.ModelForm):
    class Meta:
        model=employe
        fields='__all__'
        
