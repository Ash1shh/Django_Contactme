from django import forms
from django.forms.widgets import DateInput
from .models import users
class usersform(forms.ModelForm):
    class Meta:
        model = users
        fields = "__all__"
        labels={
            'dob':('D.O.B'),
        }
        widgets={
            'dob':DateInput(attrs={'type':'date'})
        }