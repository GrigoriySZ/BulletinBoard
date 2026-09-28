from django.urls import path
from . import views

app_name = 'notice'

urlpatterns = [
    path('', views.notice_list, name='notice_list'),
    path('notice/<int:notice_id>/', views.notice_detail, name='notice_detail'),
    path('notice/<int:notice_id>/edit/', views.edit_notice, name='edit_notice'),
    path('notice/<int:notice_id>/delete/', views.delete_notice, name='delete_notice'),
]
