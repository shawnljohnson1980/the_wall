from . import views
from django.urls import path

urlpatterns=[
    path('',views.index),
    path('log_out',views.log_out),
    path('/post_create',views.message_create),
    path('/comment_create',views.comment_create),
    path('/like',views.like)
    
]