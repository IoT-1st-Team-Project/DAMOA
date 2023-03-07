from django.http import HttpResponse
from .models import Board

from django.shortcuts import render

# Create your views here.
def index(request):
    """
    게시글 목록 출력
    """
    
    return render(request, 'main/index.html')