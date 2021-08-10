from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import auth
from django.contrib.auth.hashers import make_password, check_password
from .models import User, Diet
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


def signup(request):  # 회원가입 페이지를 보여주기 위한 함수
    if request.method == "GET":
        return render(request, 'signup.html')

    elif request.method == "POST":
        username = request.POST.get('username', None)  # 딕셔너리형태
        password1 = request.POST.get('password1', None)
        password2 = request.POST.get('password2', None)
        email = request.POST.get('email', None)
        purpose = request.POST.get('purpose', None)
        res_data = {}
        if not (username and password1 and password2 and email and purpose):
           # return HttpResponse('모든 값을 입력하십시오')
           # res_data['error'] = "모든 값을 입력해야 합니다."
            # return res_data['error']
            return render(request, 'signup.html', {'error': 'please input all data '})
        if password1 != password2:
          #  return HttpResponse('비밀번호가 다릅니다.')
           # res_data['error'] = '비밀번호가 다릅니다.'
            return render(request, 'signup.html', {'error': '비밀번호가 다릅니다. '})
        else:
            user = User(username=username, password=make_password(
                password1), email=email, purpose=purpose)
            user.save()
        # register를 요청받으면 signup.html 로 응답.
        return render(request, 'login.html', res_data)


def login(request):
    response_data = {}

    if request.method == "GET":
        return render(request, 'login.html')

    elif request.method == "POST":
        login_username = request.POST.get('username', None)
        login_password = request.POST.get('password', None)

        if not (login_username and login_password):
            response_data['error'] = "아이디와 비밀번호를 모두 입력해주세요."
        else:
            myuser = User.objects.get(username=login_username)
            # db에서 꺼내는 명령. Post로 받아온 username으로 , db의 username을 꺼내온다.
            if check_password(login_password, myuser.password):
                request.session['user'] = myuser.id
                # 세션도 딕셔너리 변수 사용과 똑같이 사용하면 된다.
                # 세션 user라는 key에 방금 로그인한 id를 저장한것.
                return redirect('home')
            else:
                response_data['error'] = "비밀번호를 틀렸습니다."

        return render(request, 'login.html', response_data)


def logout(request):
    request.session.pop('user')
    return redirect('login')


def home(request):
    user_id = request.session.get('user')
    if user_id:
        user = User.objects.get(pk=user_id)

    return render(request, 'home.html', {"user": user})


def calendar(request):
    user_id = request.session.get('user')
    if user_id:
        user = User.objects.get(pk=user_id)

    return render(request, 'calendar.html', {"user": user})


def routine(request):
    user_id = request.session.get('user')
    if user_id:
        user = User.objects.get(pk=user_id)

    return render(request, 'routine.html', {"user": user})


def community(request):
    user_id = request.session.get('user')
    if user_id:
        user = User.objects.get(pk=user_id)

    return render(request, 'community.html', {"user": user})


def diet(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    diets = Diet.objects.filter(writer=user)
    return render(request, 'diet.html', {"user" : user, "diets" : diets})


@csrf_exempt
def addDiet(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.method == 'POST':
        new_diet = Diet()
        new_diet.food = request.POST['food']
        new_diet.amount = request.POST['amount']
        new_diet.kcal = request.POST['kcal']
        new_diet.writer = user
        # new_diet.date = request.POST['date']
        new_diet.save()
    return redirect('diet', user.id)


def deleteDiet(request, user_id, diet_id):
    user = get_object_or_404(User, pk=user_id)
    delete_diet = Diet.objects.get(id=diet_id)
    delete_diet.delete()
    return redirect('diet', user.id)


def chest(request):
    user_id = request.session.get('user')
    if user_id:
        user = User.objects.get(pk=user_id)

    return render(request, 'chest.html', {"user": user})


def arm(request):
    user_id = request.session.get('user')
    if user_id:
        user = User.objects.get(pk=user_id)

    return render(request, 'arm.html', {"user": user})


def backArm(request):
    user_id = request.session.get('user')
    if user_id:
        user = User.objects.get(pk=user_id)

    return render(request, 'back-arm.html', {"user": user})


def back(request):
    user_id = request.session.get('user')
    if user_id:
        user = User.objects.get(pk=user_id)

    return render(request, 'back.html', {"user": user})


def shoulder(request):
    user_id = request.session.get('user')
    if user_id:
        user = User.objects.get(pk=user_id)

    return render(request, 'shoulder.html', {"user": user})


def leg(request):
    user_id = request.session.get('user')
    if user_id:
        user = User.objects.get(pk=user_id)

    return render(request, 'leg.html', {"user": user})


def setRoutine(request):
    user_id = request.session.get('user')
    if user_id:
        user = User.objects.get(pk=user_id)

    return render(request, 'set-routine.html', {"user": user})
