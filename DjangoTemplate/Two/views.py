from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from Two.models import Grade, Student

def students(request, g_id):

    student_list = Student.objects.filter(s_grade_id=g_id)
    return render(request,'grade_student_list.html', context=locals())


def student(request, s_id):
    print(s_id)
    print(type(s_id))
    return HttpResponse('Get Student Success')


def grades(request):

    grade_list = Grade.objects.all()
    #
    return render(request, 'grade_list.html', context=locals())


def get_time(request, hour, minute, second):

    return HttpResponse("Time %s: %s: %s" %(hour,minute,second))


def get_date(request, date, month, year):
    return HttpResponse("Date %s-%s-%s"  %(date, month,year))


def learn(request):
    return HttpResponse("你是个好孩子")


def have_request(request):
    print(request.path)
    print(request.method)
    print(request.GET)
    hobby =  request.GET.get('hobby')
    print(hobby)
    hobbies  = request.GET.getlist('hobby')
    print(hobbies)
    print(request.POST)
    print(request.META)
    for k in request.META:
        print(k, request.META.get(k))
    return HttpResponse("Request Success")


def create_student(request):
    return render(request,'student.html')


def do_create_student(request):

    print(request.method)
    username = request.POST.get('username')
    return HttpResponse(username)