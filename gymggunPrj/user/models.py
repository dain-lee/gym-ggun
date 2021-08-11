from django.db import models
from django.db.models.deletion import CASCADE

class User(models.Model):  # 장고에서 제공하는 models.Model를 상속받아야한다.
    username = models.CharField(max_length=64, verbose_name='username')
    password = models.CharField(max_length=64, verbose_name='password')
    email = models.EmailField(max_length=64, verbose_name='email')
    purpose = models.CharField(max_length=64, verbose_name='앱 사용 목적')
    registered_dttm = models.DateTimeField(
        auto_now_add=True, verbose_name='등록시간')
    # 저장되는 시점의 시간을 자동으로 삽입해준다.

    def __str__(self):
        return self.username

    class Meta:  # 메타 클래스를 이용하여 테이블명 지정
        db_table = 'test_user'

class Diet(models.Model):
    writer = models.ForeignKey(User, on_delete=CASCADE, default='')
    food = models.CharField(max_length=30)
    amount = models.CharField(max_length=20)
    kcal = models.FloatField(default=0)
    date = models.DateField(auto_now=True)

class Routine(models.Model):
    #work = models.CharField(max_length=30)
    writer = models.ForeignKey(User, on_delete=CASCADE, default='')
    mon_work1 = models.CharField(max_length=30, default='')
    mon_work2 = models.CharField(max_length=30, default='')
    mon_work3 = models.CharField(max_length=30, default='')

    tue_work1 = models.CharField(max_length=30, default='')
    tue_work2 = models.CharField(max_length=30, default='')
    tue_work3 = models.CharField(max_length=30, default='')

    wed_work1 = models.CharField(max_length=30, default='')
    wed_work2 = models.CharField(max_length=30, default='')
    wed_work3 = models.CharField(max_length=30, default='')

    thr_work1 = models.CharField(max_length=30, default='')
    thr_work2 = models.CharField(max_length=30, default='')
    thr_work3 = models.CharField(max_length=30, default='')

    fri_work1 = models.CharField(max_length=30, default='')
    fri_work2 = models.CharField(max_length=30, default='')
    fri_work3 = models.CharField(max_length=30, default='')

    sat_work1 = models.CharField(max_length=30, default='')
    sat_work2 = models.CharField(max_length=30, default='')
    sat_work3 = models.CharField(max_length=30, default='')

    sun_work1 = models.CharField(max_length=30, default='')
    sun_work2 = models.CharField(max_length=30, default='')
    sun_work3 = models.CharField(max_length=30, default='')