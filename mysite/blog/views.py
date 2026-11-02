from django.shortcuts import render

def post_list(request):
    context = {}
    return render(request, "blog/post_list.html", context)

def home(request):
    context = {}
    return render(request, "blog/home.html", context)

def about(request):
    context = {}
    return render(request, "blog/about.html", context)