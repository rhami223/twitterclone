from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .forms import TweetForm
from .models import TweetModel

from notification.models import NotificationModel
from twitteruser.models import TwitterUser
from django.views.generic import TemplateView
import re

# Create your views here.

class CreateTweet(TemplateView):
  def get(self, request):
    form = TweetForm()
    return render(request, 'tweet.html', {'form': form})

  def post(self, request):
    form = TweetForm(request.POST)
    if form.is_valid():
      data = form.cleaned_data
      tweet = TweetModel.objects.create(
        text=data.get('text'),
        posted_by=request.user,
      )
      at_tag = re.findall(r'(?<=@)\w+', data.get('text'))
      new_tweet = TweetModel.objects.create(
        text=data.get('text'),
        posted_by=request.user,
      )
      if at_tag:
        for at in at_tag:
          new_notification = NotificationModel.objects.create(
            tweet=new_tweet,
            user = TwitterUser.objects.get(username=at),)
      return HttpResponseRedirect(reverse('homepage'))




  class TwitterView(TemplateView):
    def get(self, request, tweet_id):
      tweet = TweetModel.objects.get(id=tweet_id)
      return render(request, ‘tweet_view.html’, {‘tweet’: tweet})


