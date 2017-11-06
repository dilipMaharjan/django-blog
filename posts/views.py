from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post


def post_create(request):
    return HttpResponse("posts/index")


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
