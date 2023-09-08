from django import forms
from .models import biblioteca

class formula(forms.ModelForm):
    class Meta(object):
        model = biblioteca
        fields = ('titulo',"img","des")