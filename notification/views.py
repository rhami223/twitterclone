from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .models import NotificationModel

# Create your views here.

@login_required
def notifications_view(request, user_id):
  notifications = NotificationModel.objects.filter(user_id=user_id)
  notification_alert = []
  for notification in notifications:
    if not notification.time_viewed:
      notification_alert.append(notification.tweet)
    notification.time_viewed = timezone.now()
    notification.save()
  # breakpoint()
  return render(request, 'notifications.html', {
    'notification_alert': notification_alert[::-1]}
  )