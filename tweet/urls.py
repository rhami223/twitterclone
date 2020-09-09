from django.urls import path

from tweet import views


urlpatterns = [
    path('tweet/', views.CreateTweetView.as_view()),
    path('tweet/<int:tweet_id>/', views.TwitterView.as_view()),
]