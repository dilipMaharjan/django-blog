from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
from .form import PostForm


def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.save()
    return render(request, "posts/form.html", {"form": form})


def post_detail(request, id=None):
    post = get_object_or_404(Post, id=id)
    return render(request, 'posts/detail.html', {"post": post})


def post_list(request):
    post_list = Post.objects.all()
    return render(request, "posts/index.html", {
                  "title": "List", "post_list": post_list},
                  )


def post_update(request):
    return HttpResponse("Update")


def post_delete(request):
    return HttpResponse("Delete")
