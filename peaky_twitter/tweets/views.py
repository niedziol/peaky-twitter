from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import Http404
from django.utils import timezone

from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required


def index(request):
    all_posts = Post.objects.all().order_by('-date')[:10]

    context = {'posts': all_posts}

    return render(request, 'tweets/post_list.html', context)


@login_required(login_url='/accounts/login/')
def user_tweets(request):
    posts = Post.objects.filter(author=request.user)

    context = {'posts': posts}

    return render(request, 'tweets/post_list.html', context)


def detail(request, tweet_id):
    try:
        post = Post.objects.get(pk=tweet_id)
    except Post.DoesNotExist:
        raise Http404("Tweet does not exist")
    return render(request, 'tweets/post_details.html', {'post': post})


@login_required(login_url='/accounts/login/')
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.date = timezone.now()
            post.save()
            return redirect('index')
    else:
        form = PostForm()
    return render(request, 'tweets/post_edit.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
