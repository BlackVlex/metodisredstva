from django.shortcuts import render, get_object_or_404
from .models import Post

def home(request):
    context = {}
    return render(request, "blog/home.html", context)

def post_list(request):
    posts = Post.objects.filter(is_published=True).order_by("-created_at")
    context = {
        "posts": posts
    }
    return render(request, "blog/post_list.html", context)

def about(request):
    context = {}
    return render(request, "blog/about.html", context)

# НОВАЯ ФУНКЦИЯ
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk, is_published=True)
    context = {"post": post}
    return render(request, "blog/post_detail.html", context)