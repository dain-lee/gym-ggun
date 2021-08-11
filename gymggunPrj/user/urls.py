from django.urls import path
from django.urls import path
from .views import *

urlpatterns = [
    path('', login, name='login'),
    path('home/signup/', signup, name='signup'),
    path('home/login/', login, name='login'),
    path('home/logout/', logout, name='logout'),
    path('home/mypage/calendar', calendar, name='calendar'),
    path('home/set-routine/<int:user_id>', setRoutine, name='setRoutine'),
    path('home/set-routine/add/<int:user_id>', addRoutine, name='addRoutine'),
    path('home/set-routine/delete/<int:user_id>/<int:routine_id>', deleteRoutine, name='deleteRoutine'),
    path('home/community', community, name='community'),
    path('home/diet/<int:user_id>', diet, name='diet'),
    path('home/diet/add/<int:user_id>', addDiet, name='addDiet'),
    path('home/diet/delete/<int:user_id>/<int:diet_id>', deleteDiet, name='deleteDiet'),
    path('home/chest', chest, name='chest'),
    path('home/arm', arm, name='arm'),
    path('home/back-arm', backArm, name='backArm'),
    path('home/back', back, name='back'),
    path('home/leg', leg, name='leg'),
    path('home/shoulder', shoulder, name='shoulder'),
    path('home/', home, name='home')
]
