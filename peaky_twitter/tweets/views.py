from django.shortcuts import render, redirect
from django.http import Http404
from django.utils import timezone

from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required


def index(request):
    all_posts = Post.objects.all().order_by('-date')

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
