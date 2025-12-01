from django.urls import path
from . import views

urlpatterns = [
    path('', views.notice_list, name='notice_list'),
    path('create/', views.notice_create, name='notice_create'),
    path('<int:id>/edit/', views.notice_edit, name='notice_edit'),
    path('<int:id>/delete/', views.notice_delete, name='notice_delete'),
]
