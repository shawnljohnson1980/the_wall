from django.db import models
from user_login_app.models import User




class Post(models.Model):
    content=models.CharField(max_length=500)
    creator=models.ForeignKey(User,related_name="post",on_delete=models.CASCADE)
    like=models.ManyToManyField(User,related_name='post_likes')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Comment(models.Model):
    content=models.CharField(max_length=300)
    creator=models.ForeignKey(User,related_name="comments",on_delete=models.CASCADE)
    post=models.ForeignKey(Post,related_name="comments",on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

