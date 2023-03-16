from django import forms
from main.models import Board, Club, Reply

class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['club','subject','content','event_date']
        labels={
            'club':'클럽',
            'subject':'제목',
            'content':'내용',
            'event_date':'모임일',
        }
        
class ClubForm(forms.ModelForm):
    class Meta:
        model = Club
        fields = ['category','name']
        labels={
            'category':'카테고리',
            'name':'이름',
        }   

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['content']
        labels={
            'content':'답변내용',
        }   