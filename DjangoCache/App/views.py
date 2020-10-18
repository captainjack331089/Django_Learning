import random
from time import sleep

from django.core.cache import cache, caches
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt

from App.models import Student


def hello(request):
    return HttpResponse('Hello')


#@cache_page(timeout=3)
def news(request):

    cache = caches['redis_backend']
    result = cache.get("news")
    if result:
        return HttpResponse(result)

    news_list = []
    for i in range(10):
        news_list.append("英超联赛%d" %i)
    sleep(5)
    data = {
        'news_list': news_list,
    }

    response = render(request, 'news.html', context=data)
    cache.set('news',response.content, timeout=60)
    return response

@cache_page(60,cache='default')
def jokes(request):
    sleep(3)
    return HttpResponse('Joke List')


def home(request):
    return HttpResponse('HOME')


def get_phone(request):
    if random.randrange(100) > 95:
        return  HttpResponse('恭喜你抢到supreme')
    return HttpResponse('正在排队')


def get_ticket(request):
    return HttpResponse("还剩99张")


def search(request):
    return HttpResponse('这是你cop到的资源')


def calc(request):

    a = 250
    b = 250
    result = (a+b) / 0
    return HttpResponse(result)

@csrf_exempt
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        return HttpResponse("登录成功")


def add_students(request):
    for i in range(100):

        student = Student()
        student.s_name = 'Jack %d' %i
        student.s_age = i
        student.save()
    return HttpResponse(' Student create success')

def get_students(request):

    #原始分页方法
    page = int(request.GET.get('page', 1))
    per_page =  int(request.GET.get('per_page', 10))
    students = Student.objects.all()[per_page*(page-1) : page*per_page]

    #students = Student.objects.all()
    data = {
        'students': students,
    }
    return render(request, 'students.html', context=data)


def get_students_with_page(request):

    students = Student.objects.all()
    page = int(request.GET.get('page', 1))
    per_page =  int(request.GET.get('per_page', 10))

    paginator = Paginator(students, per_page)
    page_object = paginator.page(page)


    data = {
        'page_object': page_object,
        'page_range': paginator.page_range,
    }

    return render(request, 'students_with_page.html', context=data)