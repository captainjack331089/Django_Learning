import random

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse


def hello(request):

    response = HttpResponse()
    # response.content = 'aj'
    # response.status_code = 404
    response.write('听说你很帅')
    response.flush()

    return response


def get_ticket(request):


    url = reverse('app:hello')
    if random.randrange(10) > 5:

        # return HttpResponseRedirect(url)
        return redirect(url)
    else:
        return HttpResponse('恭喜你抢到票了')


def get_info(request):
    data  = {
        "status":200,
        "msg": "ok",
    }
    return JsonResponse(data=data)


def set_cookie(request):
    response =  HttpResponse("设置cookie")
    response.set_cookie('username','jack')
    return response


def get_cookie(request):
    username = request.COOKIES.get('username')
    return HttpResponse(username)


def login(request):
    return render(request, 'login.html' )


def do_login(request):
    uname= request.POST.get('uname')
    response = HttpResponseRedirect(reverse('app:mine'))
    # response.set_cookie('uname', uname,max_age=60)
    response.set_signed_cookie('content', uname, 'Jackie')
    return response


def mine(request):
    # uname = request.COOKIES.get('content')
    try:
        uname = request.get_signed_cookie('content', salt='Jackie')
        if uname:
            # return HttpResponse(uname)
            return render(request, 'mine.html', context={"uname": uname})

    except Exception as e:
        print("获取失败")
    return redirect(reverse('app:login'))


def logout(request):

    response = redirect(reverse('app:login'))
    response.delete_cookie("content")
    return response