 
from django.urls import path

from twitteruser import views


urlpatterns = [
    path('', views.index, name='homepage'),
    path('signup/', views.create_user, name='signup'),
    path('follow/', views.following_view, name='follow'),
    path('profile/<int:user_id>/', views.user_profile, name='profile'),
]