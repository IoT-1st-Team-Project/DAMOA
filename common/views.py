from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import CustomUserForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash, logout
from django.contrib import messages


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

@login_required(login_url='common:login')
def change_password(request):
  if request.method == "POST":
    form = PasswordChangeForm(request.user, request.POST)
    if form.is_valid():
      user = form.save()
      update_session_auth_hash(request, user)
      logout(request) # 변경 성공시 로그아웃
      messages.success(request, '비밀번호가 변경되었습니다. 다시 로그인 해주세요')
      return redirect('common:login')
    else:
      messages.error(request, '비밀번호 변경에 실패하였습니다.')
  else:
    form = PasswordChangeForm(request.user)
  return render(request, 'common/change_password.html',{'form':form})