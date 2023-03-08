from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# 회원가입에 사용할 UserForm (UserCreateionForm을 상속)
# UserCreateionForm은 username(이름), pw1, pw2 속성을 가짐

class UserForm(UserCreationForm):
    # email 속성 추가
    email = forms.EmailField(label="이메일")
    userid = forms.CharField(max_length = 15, label="아이디")
    age = forms.IntegerField(label="나이")
    ad = forms.CharField(max_length = 50, label="거주지")
    '''
    GENDERS = (
        ('M', '남성(Man)'),
        ('W', '여성(Woman)'),
    )

    gender = models.CharField(verbose_name='성별', max_length=1, choices=GENDERS)
    '''

    class Meta:
        model = User
        fields = ("userid", "username", "password1", "password2", "email", "age", "ad")
        # fields = ("userid", "username", "password1", "password2", "email", "age", "ad", "gender")