from django.urls import path, include
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('main/', views.main, name='main'),
    path('main/board_list/', views.board_list, name='board_list'),
    path('main/board_list/<int:board_id>/', views.detail, name='datail'),

]