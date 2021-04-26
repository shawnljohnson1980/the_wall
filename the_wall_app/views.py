from django.shortcuts import render, redirect
from user_login_app.models import User
from .models import Post, Comment


# Create your views here.
def index(request):
    post=Post.objects.all()
    comment=Comment.objects.all()
    user=User.objects.get(id=request.session['user_id'])
    context={
        'user':user,
        'comments':comment,
        'posts':post,
    }
    return render(request, 'index.html',context)
    

def comment_create(request):
    post=Post.objects.get(id=request.POST['post_id'])
    user=User.objects.get(id=request.session['user_id'])
    Comment.objects.create(
        content=request.POST['content'],
        creator=user,
        post=post
    )
    return redirect('/the_wall')


def message_create(request):
    user=User.objects.get(id=request.session['user_id'])
    Post.objects.create(
    content=request.POST['content'],
    creator=user,
    
    )
    return redirect('/the_wall')



def like(request):
        user = User.objects.get(id=request.session['user_id'])
        post = Post.objects.get(id=request.POST['post_id'])
        like = post.like
        like.alreadyLiked = True
        post.like.add(user)
        post.save()
        return redirect('/the_wall')

def delete(request,post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect('/the_wall')

def log_out(request):
    request.session.flush()
    return redirect('/')
