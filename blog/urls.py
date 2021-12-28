from django.urls import path

from . import views

urlpatterns = [
    # 예시: /blog/
    path('', views.index, name='index'),
]