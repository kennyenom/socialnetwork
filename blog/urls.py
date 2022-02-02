from django.urls import path
from .import views


urlpatterns = [
    path('',views.index,name='blog-home'),
    path('about/',views.about,name='blog-about'),
    path('new/',views.newpost,name='blog-post'),
    path('detail/<int:pk>',views.post_detail,name='blog-detail'),
    path('delete/<int:pk>',views.post_delete,name='blog-post-delete'),
    path('edit/<int:pk>',views.post_edit,name='blog-post-edit'),
]