from django.urls import path
from tyoubo import views

app_name = 'tyoubo'
urlpatterns = [
    path('post/create/', views.create_post, name='create_post'),  # 作成
    path('post/edit/<int:item_id>/', views.edit_post, name='edit_post'),  # 修正
    path('post/', views.read_post, name='read_post'),   # 一覧表示
    path('', views.read_post, name='read_post'),   # 一覧表示
    path('post/delete/<int:item_id>/', views.delete_post, name='delete_post'),   # 削除
]