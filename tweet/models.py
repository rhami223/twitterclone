from django.db import models
from django.utils import timezone

from twitteruser.models import TwitterUser

# Create your models here.

class TweetModel(models.Model):
  text = models.CharField(max_length=140)
  date_filed = models.DateTimeField(default=timezone.now)
  posted_by = models.ForeignKey(
    TwitterUser,
    on_delete=models.CASCADE,
  )