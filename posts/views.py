from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages

from .models import Post
from .form import PostForm

def post_create(request):
    form=PostForm(request.POST or None)
    if form.is_valid():
        instance=form.save(commit= False)
        instance.save()
        messages.success(request,"Post Created.")
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request,"Post Creation Failed.")

    return render(request,"posts/form.html",{"form":form})

def post_detail(request, id=None):
    post = get_object_or_404(Post, id=id)
    return render(request, 'posts/detail.html', {"post": post})


def post_list(request):
    post_list = Post.objects.all()
    return render(request, "posts/index.html", {
                  "title": "List", "post_list": post_list},
                  )


def post_update(request,id=None):
    instance=get_object_or_404(Post,id=id)
    form=PostForm(request.POST or None,instance=instance)
    if form.is_valid():
        instance=form.save(commit= False)
        instance.save()
        messages.success(request,"Post Updated.")
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request,"Post update Failed.")
    return render(request,"posts/form.html",{"form":form})

def post_delete(request):
    return HttpResponse("Delete")
