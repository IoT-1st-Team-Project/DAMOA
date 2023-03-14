from .models import Club, Board
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.utils import timezone
from .forms import BoardForm, ClubForm

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

    # 입력 인자
    page = request.GET.get('page', '1')  # 페이지
    board_list = Board.objects.order_by('-create_date')
    paginator = Paginator(board_list, 5)  # 페이지당 5개 테스트
    page_obj = paginator.get_page(page)
    context = {'board_list':page_obj}

    return render(request, 'main/board_list.html', context)



def detail(request, board_id):
    '''
    board내용 출력
    '''
    board=get_object_or_404(Board, pk=board_id)
    context={'board':board}
    return render(request, 'main/board_detail.html',context)


def login(request):
    """
    로그인 화면 출력
    """
    
    return render(request, 'templates/common/login.html')   


def reply_create(request, board_id):
    '''
    댓글등록
    '''
    board=get_object_or_404(Board, pk=board_id)
    board.reply_set.create(content=request.POST.get('content'),create_date=timezone.now())
    return redirect('main:detail', board_id=board.id)

def board_create(request):
    '''
    게시글등록
    '''
    if request.method=='POST':
        form=BoardForm(request.POST)
        if form.is_valid():
            board=form.save(commit=False)
            board.create_date=timezone.now()
            board.save()
            return redirect('main:board_list')
    else:
        form=BoardForm()
            
    return render(request, 'main/board_form.html', {'form':form})

def club_create(request):
    '''
    클럽등록
    '''
    if request.method=='POST':
        form=ClubForm(request.POST)
        if form.is_valid():
            club=form.save(commit=False)
            club.save()
            return redirect('main:main')
    else:
        form=ClubForm()
    return render(request, 'main/club_form.html', {'form':form})
    