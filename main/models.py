from django.db import models
from django.contrib.auth.models import User

# 게시글 모델
class Board(models.Model):
    # author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='board_author')
    subject = models.CharField('제목', max_length = 200,
                               help_text='게시글의 제목을 한 줄로 작성하세요.')
    content = models.TextField('내용', help_text='내용을 상세히 작성하세요.')
    create_date = models.DateTimeField('생성일')
    # modify_date = models.DateTimeField(null=True, blank=True)
    # like = models.ManyToManyField(User, related_name='borad_like')

    def __str__(self):
        return self.subject

# 댓글 모델
class Reply(models.Model):
    board = models.ForeignKey(Board, on_delete = models.CASCADE)  # 게시글 삭제되면 댓글도 삭제
    content = models.TextField()
    create_date = models.DateTimeField('생성일')
    # modify_date = models.DateTimeField(null=True, blank=True)
    # like = models.ManyToManyField(User, related_name='reply_like')
