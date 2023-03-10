from django.urls import path, include
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('main/', views.main, name='main'),
    path('main/board/', views.board_list, name='board_list'),
    path('main/board/<int:board_id>/', views.detail, name='datail'),
    path('main/board/create/', views.board_create, name='board_create'),
    path('main/board/create/<int:board_id>/', views.reply_create, name='reply_create'),

]