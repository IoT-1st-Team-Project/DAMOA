from django.http import HttpResponse
# from .models import Board

from django.shortcuts import render
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    """
    첫 화면 출력
    """
    
    return render(request, 'main/index.html')

def main(request):
    """
    메인 화면 출력
    """
    
    return render(request, 'main/main.html')

def login(request):
    """
    로그인 화면 출력
    """
    
    return render(request, 'templates/common/login.html')

# def Clublist(request):
    