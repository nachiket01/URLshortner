from nturl2path import url2pathname
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='índex'),
    path('create',views.create,name='create'),
    path('<str:pk>',views.go,name='go'),
    ] 