from .models import Club, Board
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.utils import timezone
from .forms import BoardForm

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

def board_create(request):
    '''board생서'''
    if request.method=='POST':
        form = BoardForm(request.POST)
        if form.is_valid:
            board=form.save(commit=False)
            board.create_date=timezone.now()
            board.save()
            return redirect('main:board_list')
    else:
        form = BoardForm()
    
    return render(request, 'main/board_form.html', {'form':form})


def detail(request, board_id):
    '''
    board내용 출력
    '''
    board=get_object_or_404(Board, pk=board_id)
    context={'board':board}
    return render(request, 'main/board_datail.html',context)


def login(request):
    """
    로그인 화면 출력
    """
    
    return render(request, 'templates/common/login.html')   

def reply_create(request, board_id):
    '''
    댓글 등록
    '''
    board=get_object_or_404(Board, pk=board_id)
    board.reply_set.create(content=request.POST.get('content'),
                           create_date=timezone.now())
    
    return redirect('main:detail',board_id=board.id)