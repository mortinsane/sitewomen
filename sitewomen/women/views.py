from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import redirect
from django.urls import reverse

# Create your views here.
def index(request):
    return HttpResponse('страница приложения women.')


def categories(request, cat_id):
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>id: {cat_id}</p>')

def categories_by_slug(request, cat_slug):
    if request.GET:
        print(request.GET)
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>slug: {cat_slug}</p>')

def archive(request, year):
    if year > 2023:
        # raise Http404()
        # return redirect('/', permanent=True)
        # return redirect(index, permanent=True) # функция представления
        uri = reverse('cats',args=('music',))
        return redirect(uri) # имя маршрута
    return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')

def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


