from django import forms
from main.models import Board, Club, Reply
# from bootstrap_datepicker_plus import DatePickerInput

class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['club','subject','content','event_date']
        widgets = {
            'subject': forms.TextInput(attrs={'placeholder': '제목을 입력하세요.'}),
            'content': forms.Textarea(attrs={'placeholder': '내용을 입력하세요.'}),
            # 'event_date': DatePickerInput(format='%Y-%m-%d'),
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