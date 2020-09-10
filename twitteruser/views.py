from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from tweet.models import TweetModel

from notification.models import NotificationModel

from authentication.views import login_view

from .forms import SignUpForm

from .models import TwitterUser

# Received help from Matt Perry and Peter Marsh on many little errors throughout the code.
# Got guidance from StackOverFlow about ManyToManyField

@login_required
def index(request):
  tweets = TweetModel.objects.filter(posted_by=request.user)
  following_tweets = TweetModel.objects.filter(posted_by__in=request.user.following.all())
  user_following_tweets = tweets | following_tweets
  user_following_tweets = user_following_tweets.order_by('-date_filed')
  count = len(
      [notified for notified in NotificationModel.objects.filter(user_id=request.user.id) if not notified.time_viewed]
      )
  return render(request, 'index.html',
      {
        "tweets": user_following_tweets,
        "count": count
      })


def create_user(request):
  if request.method == "POST":
    form = SignUpForm(request.POST)
    if form.is_valid():
      data = form.cleaned_data
      new_user = TwitterUser.objects.create_user(
        username=data.get('username'),
        password=data.get('password'),
      )
      if new_user:
        login(request, new_user)
        return HttpResponseRedirect(reverse('home'))
  form = SignUpForm()
  return render(request, 'generic_form.html', {'form': form})


def user_profile(request, user_id):
  profile = TwitterUser.objects.get(id=user_id)
  tweets = TweetModel.objects.filter(posted_by=profile)
  following = request.user.following.all()
  following_list = list(following)
  return render(request, "profile.html",
    {
      "profile": profile,
      "tweets": tweets,
      "user_following": following_list
    }
  )


@login_required
def following_view(request, following_id):
    current_user = request.user
    follow = TwitterUser.objects.filter(id=following_id).first()
    current_user.following.add(follow)
    return HttpResponseRedirect(reverse('home'))


@login_required
def unfollow_view(request, unfollow_id):
    current_user = request.user
    follow = TwitterUser.objects.filter(id=unfollow_id).first()
    current_user.following.remove(follow)
    return HttpResponseRedirect(reverse('home'))