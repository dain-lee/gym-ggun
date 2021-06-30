from django.urls import path
from django.urls import path
from .views import *

urlpatterns = [
    path('home/signup/', signup, name='signup'),
    path('home/login/', login, name='login'),
    path('home/logout/', logout, name='logout'),
    path('home/mypage/calendar', calendar, name='calendar'),
    path('home/mypage/routine', routine, name='routine'),
    path('home/', home, name='home')
]
