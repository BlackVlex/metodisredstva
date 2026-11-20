from django.shortcuts import redirect, render, get_object_or_404
from .models import Post
from .forms import PostForm

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

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk, is_published=True)
    context = {"post": post}
    return render(request, "blog/post_detail.html", context)

def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect("post_detail", pk=post.pk)
    else:
        form = PostForm()
    
    context = {"form": form}
    return render(request, "blog/post_form.html", context)

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect("post_detail", pk=post.pk)
    else:
        form = PostForm(instance=post)
    
    context = {"form": form, "post": post}
    return render(request, "blog/post_form_edit.html", context)

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if request.method == "POST":
        post.delete()
        return redirect("post_list")
    
    context = {"post": post}
    return render(request, "blog/post_confirm_delete.html", context)