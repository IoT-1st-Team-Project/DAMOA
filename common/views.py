from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from .forms import CustomUserForm


def signup(request):
    """
    회원가입
    """
    if request.method == "POST":
        form = CustomUserForm(request.POST)  # 새로운 사용자 생성
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')  # 회원가입 화면에서 입력한 값을 얻어와
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password) # 사용자 인증
            # 자동로그인 삭제 (오류남)
            return redirect('common:login')
    else:
        form = CustomUserForm()
    return render(request, 'common/signup.html', {'form': form})
