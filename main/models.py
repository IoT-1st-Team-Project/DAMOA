from django.db import models
# from django.contrib.auth.models import User

class Club(models.Model):
    # owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='club_owner')
    class category(models.TextChoices):
        from django.utils.translation import gettext_lazy as _
        COOK = 'CK', _('Cook')
        CULTURE = 'CT', _('Culture')
        GAME = 'GA', _('Game')
        LANGUAGE = 'LA', _('Language')
        MUSIC = 'MU', _('Music')
        OUTDOOR = 'OD', _('Outdoor')
        SPORTS = 'SP', _('Sports')
        
    category = models.CharField(
        max_length=10,
        choices = category.choices,
        null=True
    )
   
    name=models.TextField('클럽이름')

    def __str__(self):
        return self.name



# # 게시글 모델
# class Board(models.Model):
#     # author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='board_author')
#     subject = models.CharField('제목', max_length = 200,
#                                help_text='게시글의 제목을 한 줄로 작성하세요.')
#     content = models.TextField('내용', help_text='내용을 상세히 작성하세요.')
#     create_date = models.DateTimeField('생성일')
#     modify_date = models.DateTimeField(null=True, blank=True)
#     # event_date = models.DateTimeField(null=False, blank=False)
#     # like = models.ManyToManyField(User, related_name='club_like')
#     category = models.ForeignKey(Club, on_delete=models.CASCADE)


#     def __str__(self):
#         return self.id, self.subject


# # 댓글 모델
# class Reply(models.Model):
#     # author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reply_author')
#     club_id = models.ForeignKey(Club, on_delete = models.CASCADE)  # 게시글 삭제되면 댓글도 삭제
#     content = models.TextField()
#     create_date = models.DateTimeField('생성일')
#     modify_date = models.DateTimeField(null=True, blank=True)
#     # like = models.ManyToManyField(User, related_name='reply_like')

#     def __str__(self):
#         return self.content
