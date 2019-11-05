from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('my_tweets', views.user_tweets, name='my_tweets'),
    path('<int:tweet_id>/', views.detail, name='detail'),
]