from django.shortcuts import get_object_or_404, render, redirect
from .models import *
from django.contrib import messages
from .forms import UserRegisterForm, PostForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def feed(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'social/feed.html', context)


def profile(request, username=None):
    current_user = request.user
    if username and username != current_user.username:
        user = User.objects.get(username=username)
        posts = user.posts.all()
    
    else:
        posts = current_user.posts.all()
        user = current_user
    return render(request, 'social/profile.html', {'user': user, 'posts': posts})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'User {username} was successfully registered')
            return redirect('feed')

    else:
        form = UserRegisterForm()
    
    context = {'form': form}
    return render(request, 'social/register.html', context)

@login_required
def post(request):
    curent_user = get_object_or_404(User, pk=request.user.pk)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = curent_user
            post.save()
            messages.success(request, 'Post saved successfully')
            return redirect('feed')
    
    else:
        form = PostForm()
    
    return render(request, 'social/post.html', {'form': form})


def follow(request, username):
    current_user = request.user
    to_user = User.objects.get(username=username)
    to_user_id = to_user
    rel = Relationship(from_user=current_user, to_user=to_user_id)
    rel.save()
    messages.success(request, f'You are following to {username}')

    return redirect('profile',username)

def unfollow(request, username):
    current_user = request.user
    to_user = User.objects.get(username=username)
    to_user_id = to_user.id
    rel = Relationship.objects.filter(from_user=current_user.id, to_user=to_user_id).get()
    rel.delete()
    messages.success(request, f'You unfollow {username}')

    return redirect('profile', username)
