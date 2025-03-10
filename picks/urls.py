# picks/urls.py
from django.urls import path
from . import views
from .views import schedule_view

app_name = 'picks'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.home, name='home'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('view_picks/<int:user_id>/', views.view_picks, name='view_picks'),

]

