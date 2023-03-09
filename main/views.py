from .models import Club, Board
from django.shortcuts import render, get_object_or_404
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
    club_list=Club.objects.order_by('-id')
    context={'club_list':club_list}
    return render(request, 'main/main.html', context)


def board_list(request):
    '''
    board 출력
    '''
    board_list=Board.objects.order_by('-id')
    context={'board_list':board_list}
    return render(request, 'main/board_list.html',context)

def detail(request, board_id):
    '''
    board내용 출력
    '''
    board=get_object_or_404(Board, pk=board_id)
    context={'board':board}
    return render(request, 'main/board_datail.html',context)