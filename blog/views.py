from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView

# Create your views here.
class PostList(ListView):
    model = Post
    ordering = '-pk'
    # 템플릿 모델명_list.html : post_list.html **자동 생성
    # 파라미터 모델명_list : post_list

class PostDetail(DetailView):
    model = Post #**데이터 한 개라 ordering 안 함
    # 템플릿 모델명_detail.html : post_detail.html
    # 파라미터 모델명 : post

#def index(request):
#    posts1 = Post.objects.all().order_by('-pk')
#    return render(request, 'blog/index.html', {'posts' : posts1}) # 오른쪽은 위에서 준비된 변수값

#def single_post_page(request, pk):
#    post2 = Post.objects.get(pk=pk)
#    return render(request, 'blog/single_post_page.html', {'post': post2})