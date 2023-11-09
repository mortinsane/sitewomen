﻿from django.urls import path, re_path, register_converter
from . import views
from . import converters


register_converter(converters.FourDigitYearConverter, 'year4')

urlpatterns = [
    path('', views.index),
    path('cat/<int:cat_id>/', views.categories),  # http://127.0.0.1:8000/cat/
    path('cat/<slug:cat_slug>/', views.categories_by_slug),  # http://127.0.0.1:8000/cat/
    # re_path(r'^archive/(?P<year>[0-9]{4})/', views.archive)
    path('archive/<year4:year>/', views.archive),

]