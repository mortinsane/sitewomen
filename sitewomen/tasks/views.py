from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404


# Create your views here.

def post_detail(request):
    if request.GET:
        s = "|".join([f"{k}={v}"for k, v in request.GET.items()])
        return HttpResponse(s)
    

def posts_list(request, year):
    if 1990 <= year <= 2023:
        return HttpResponse(f'posts: {year}')
    raise Http404()

def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')