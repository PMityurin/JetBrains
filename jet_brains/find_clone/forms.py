from django import forms
from .models import New_File


class UserForm(forms.ModelForm):

    class Meta:
        model = New_File
        fields = ['title', 'file']