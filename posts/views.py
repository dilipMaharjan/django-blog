from django.shortcuts import render
from django.http import HttpResponse


def post_create(request):
    return HttpResponse("Post Create")


def post_detail(request):
    return HttpResponse("Detail")


def post_list(request):
    return HttpResponse("List")


def post_update(request):
    return HttpResponse("Update")


def post_delete(request):
    return HttpResponse("Delete")
