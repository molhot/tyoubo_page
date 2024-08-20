from django.shortcuts import render, get_object_or_404, redirect
from django.forms import ModelForm

from tyoubo.models import TyouboConfig


def create_post(request):
    """
    新たなデータを作成する
    """
    regist_item_obj = TyouboConfig()
    if request.method == 'GET':
        form = PostForm(instance=regist_item_obj)
        return render(request, 'tyoubo_app/post_form.html', {'item': form})
    if request.method == 'POST':
        form = PostForm(request.POST, instance=regist_item_obj)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
        return redirect('tyoubo_app:read_post')

def read_post(request):
    """
    データの一覧を表示する
    """
    tyoubo_items = TyouboConfig.objects.all().order_by('id')
    return render(request,'tyoubo_app/item_list.html',  {'items': tyoubo_items})

def edit_post(request, item_id):
    """
    対象のデータを編集する
    """
    edit_item = get_object_or_404(TyouboConfig, pk=item_id)
    if request.method == 'GET':
        item = PostForm(instance=edit_item)
        return render(request, 'tyoubo_app/post_form.html', {'item': item, 'item_id': item_id})
    elif request.method == 'POST':
        item = PostForm(request.POST, instance=edit_item)
        if item.is_valid():
            post = item.save(commit=False)
            post.save()
        return redirect('tyoubo_app:read_post')

def delete_post(request, item_id):
    post = get_object_or_404(TyouboConfig, pk=item_id)
    post.delete()
    return redirect('tyoubo_app:read_post')


class PostForm(ModelForm):
    """
    フォーム定義
    """
    class Meta:
        model = TyouboConfig
        fields = ('item_name', 'item_price', 'item_price', 'item_type')
