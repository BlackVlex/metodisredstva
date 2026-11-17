from django.shortcuts import render
from .models import Post

def post_list(request):
    post = Post.objects.filter(is_published=True).order_by("-created_at")
    context = {
        "posts": post
    }
    return render(request, "blog/post_list.html", context)

def home(request):
    context = {}
    return render(request, "blog/home.html", context)

def about(request):
    context = {}
    return render(request, "blog/about.html", context)
