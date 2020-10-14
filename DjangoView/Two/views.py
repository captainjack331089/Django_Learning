import hashlib
import random
import time

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from Two.models import Student


def hello(request):
    return HttpResponse('Hello Two')


def login(request):
    if request.method == 'GET':
        return render(request, 'two_login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        request.session['username'] = username
        # return  HttpResponse('登录成功')
        response =  redirect(reverse('two:mine'))
        return response

def mine(request):
    username = request.session.get('username')
    return render(request, 'two_mine.html', context=locals())


def logtout(request):

    response = redirect(reverse('two:mine'))
    # response.delete_cookie('sessionid')
    # del request.session['username']

    ##session，cookie一起删
    request.session.flush()
    return response


def register(request):
    if request.method == "GET":
        return render(request, 'student_register.html')
    elif  request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            student = Student()
            student.s_name = username
            student.s_password = password
            student.s_token = 'default'
            student.save()
            print('success')

        except Exception as e:
            print('sss')
            return redirect(reverse('two:register'))

        return HttpResponse("注册成功 ")


def student_login(request):
    if request.method == 'GET':
        return render(request, 'student_login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        students = Student.objects.filter(s_name=username).filter(s_password=password)
        if students.exists():
            student = students.first()
            ip = request.META.get("REMOTE_ADDR")
            token = generate_token(ip, username)
            student.s_token = token
            student.save()
            response = HttpResponse("用户登录成功")
            response.set_cookie('token', token)
            return response
        return redirect(reverse('two:student_login'))

def generate_token(ip, username):
    c_time = time.ctime()
    r = username
    return hashlib.new("md5", (ip + c_time + r).encode('utf-8')).hexdigest()


def student_mine(request):

    token = request.COOKIES.get('token')
    try:
        student = Student.objects.get(s_token=token)

    except Exception as e:
        return redirect(reverse("two:student_login"))

    return  HttpResponse(student.s_name)

    return None