from django.shortcuts import render
from django.http import Http404
from django.template import loader
from tweets.models import Post
from django.contrib.auth.decorators import login_required


def index(request):
    all_posts = Post.objects.all().order_by('-date')

    context = {'all_posts': all_posts}

    return render(request, 'tweets/index.html', context)


@login_required(login_url='/accounts/login/')
def user_tweets(request):
    posts = Post.objects.filter(author=request.user)

    context = {'posts': posts}

    return render(request, 'tweets/my_tweets.html', context)


def detail(request, tweet_id):
    try:
        tweet = Post.objects.get(pk=tweet_id)
    except Post.DoesNotExist:
        raise Http404("Tweet does not exist")
    return render(request, 'tweets/detail.html', {'tweet': tweet})