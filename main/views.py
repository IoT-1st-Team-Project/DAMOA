from .models import Club, Board
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .forms import BoardForm, ClubForm, ReplyForm
from django.contrib import messages

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


def board_create(request):
    '''
    게시글등록
    '''
    if request.method=='POST':
        form=BoardForm(request.POST)
        if form.is_valid():
            board=form.save(commit=False)
            board.create_date = timezone.now()
            board.save()
            return redirect('main:board_list')
    else:
        form=BoardForm()
            
    return render(request, 'main/board_form.html', {'form':form})


@login_required(login_url = 'common:login')
def board_modify(request, board_id):
    """
    main 게시글 수정
    """
    board = get_object_or_404(Board, pk = board_id)
    if request.user != board.author:
        messages.error(request, '수정 권한이 없습니다.')
        return redirect('main:detail', board_id = board.id)
    
    if request.method == 'POST':
        form = BoardForm(request.POST, instance = board)
        if form.is_valid():
            board = form.save(commit = False)
            board.author = request.user
            board.modify_date = timezone.now()
            board.save()
            return redirect('main:detail', board_id = board.id)
    else:
        form = BoardForm(instance=board)  # 기존 내용이 반영된 상태에서 수정 시작
    context = {'form': form}
    return render(request, 'main/board_form.html', context)

@login_required(login_url = 'common:login')
def board_delete(request, board_id):
    """
    main 게시글 삭제
    """
    board = get_object_or_404(Board, pk = board_id)
    if request.user != board.author:
        messages.error(request, '삭제 권한이 없습니다.')
        return redirect('main:detail', board_id = board.id)
    board.delete()
    return redirect('main:index')


def reply_create(request, board_id):
    '''
    댓글등록
    '''
    board=get_object_or_404(Board, pk=board_id)
    if request.method=='POST':
        form=ReplyForm(request.POST)
        if form.is_valid():
            reply=form.save(commit=False)
            reply.create_date=timezone.now()
            reply.board=board
            reply.save()
            return redirect('main:detail', board_id=board.id)
    else:
        form=ReplyForm()
    context={'board':board, 'form':form}            
    return render(request, 'main/board_detail.html', context)



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
    