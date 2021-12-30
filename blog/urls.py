from django.urls import path

from . import views

urlpatterns = [
    # /blog
    path('', views.index, name='index'),
    path('post/<str:filename>', views.post, name='post'),
]