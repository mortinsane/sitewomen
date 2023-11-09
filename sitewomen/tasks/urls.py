from django.urls import path, re_path, register_converter
from . import views




urlpatterns = [
    path('post_detail/', views.post_detail),
    path('posts_list/<int:year>/', views.posts_list),

]