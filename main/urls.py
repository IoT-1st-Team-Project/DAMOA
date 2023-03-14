from django.urls import path, include
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('main/', views.main, name='main'),
    path('main/board_list/', views.board_list, name='board_list'),
    path('main/board_list/<int:board_id>/', views.detail, name='detail'),
    path('main/board_list/board/create/', views.board_create, name='board_create'),
    path('main/board_list/reply/create/<int:board_id>/', views.reply_create, name='reply_create'),
 
]