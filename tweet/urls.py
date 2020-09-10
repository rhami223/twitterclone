from django.urls import path

from tweet import views


urlpatterns = [
    path('tweet/', views.create_tweet),
    path('tweet/<int:tweet_id>/', views.tweet_view),
]