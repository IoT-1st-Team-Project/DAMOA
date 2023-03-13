from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


# 회원가입에 사용할 UserForm (UserCreateionForm을 상속)
# UserCreateionForm은 username(이름), pw1, pw2 속성을 가짐

class CustomUserForm(UserCreationForm):

    class Meta(UserCreationForm.Meta) :
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('name', 'email', 'age', 'ad')
        