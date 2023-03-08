from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from .forms import UserForm


def signup(request):
    """
    회원가입
    """
    if request.method == "POST":
        form = UserForm(request.POST)  # 새로운 사용자 생성
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')  # 회원가입 화면에서 입력한 값을 얻어와
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)  # 회원가입되면 자동 로그인
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})