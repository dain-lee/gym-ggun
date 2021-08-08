from django.urls import path
from django.urls import path
from .views import *

urlpatterns = [
    path('home/signup/', signup, name='signup'),
    path('home/login/', login, name='login'),
    path('home/logout/', logout, name='logout'),
    path('home/mypage/calendar', calendar, name='calendar'),
    path('home/set-routine', setRoutine, name='setRoutine'),
    path('home/community', community, name='community'),
    path('home/diet/<int:user_id>', diet, name='diet'),
    path('home/chest', chest, name='chest'),
    path('home/arm', arm, name='arm'),
    path('home/back-arm', backArm, name='backArm'),
    path('home/back', back, name='back'),
    path('home/leg', leg, name='leg'),
    path('home/shoulder', shoulder, name='shoulder'),
    path('home/', home, name='home')
]
