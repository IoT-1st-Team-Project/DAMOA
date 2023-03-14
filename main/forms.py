from django import forms
from main.models import Board, Reply

class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['club','subject','content']
        labels={
            'club':'클럽',
            'subject':'제목',
            'content':'내용',
        }



class AnswerForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['subject','content']
        labels={
            'subject':'제목',
            'content':'내용',
        }
