from django.forms import ModelForm
from django import forms
from main.models import Board

class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['subject','content']

    widgets={
        'subject':forms.TextInput(attrs={'class':'form-control'}),
        'content':forms.Textarea(attrs={'class':'form-control', 'rows':10}),
    }
    labels={
        'subject':'제목',
        'content':'내용',
    }
