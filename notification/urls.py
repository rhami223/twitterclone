from django.urls import path
from .views import notifications_view

urlpatterns = [
    path('notifications/<int:user_id>/', notifications_view)
]