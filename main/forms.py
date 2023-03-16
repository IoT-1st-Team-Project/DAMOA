from django import forms
from main.models import Board, Club, Reply
from django_summernote.widgets import SummernoteWidget

class BoardForm(forms.ModelForm):
    content = forms.CharField(widget=SummernoteWidget())

    class Meta:
        model = Board
        fields = ['club','subject','content','event_date']
        widgets = {
            'subject': forms.TextInput(attrs={'placeholder': '제목을 입력하세요.'}),
            'content': forms.Textarea(attrs={'placeholder': '내용을 입력하세요.'}),
            'event_date': forms.DateTimeInput(attrs={'placeholder': '2023-03-16 14:03 형식'},format='%Y-%m-%d'),
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