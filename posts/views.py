from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from .form import PostForm
from .models import Post


def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Post Created.")
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request, "Post Creation Failed.")

    return render(request, "posts/form.html", {"form": form})


def post_detail(request, id=None):
    post = get_object_or_404(Post, id=id)
    return render(request, 'posts/detail.html', {"post": post})


def post_list(request):
    post_list = Post.objects.all()

    paginator = Paginator(post_list, 2)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)

    return render(request, "posts/index.html", {
        "title": "List", "post_list": posts})


def post_update(request, id=None):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Post Updated.")
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request, "Post update Failed.")
    return render(request, "posts/form.html", {"form": form})


def post_delete(request, id=None):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request, "Successfully deleted.")
    return redirect("list")
