from django.contrib.auth.hashers import make_password, check_password
from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from App.models import MainWheel, MainNav, MainMustBuy, MainShop, Mainshow, FoodType, Goods, AAAUser
from App.views_constant import ALL_TYPE, ORDER_TOTAL, ORDER_PRICE_UP, ORDER_PRICE_DOWN, ORDER_SALE_UP, ORDER_SALE_DOWN, \
    HTTP_USER_EXIST, HTTP_OK, HTTP_EMAIL_EXIST
from App.views_helper import hash_str
from ShoppingSite.settings import MEDIA_KEY_PREFIX


def home(request):
    main_wheels = MainWheel.objects.all()
    main_navs = MainNav.objects.all()
    main_mustbuys = MainMustBuy.objects.all()
    main_shops = MainShop.objects.all()

    main_shop0_1 = main_shops[0:1]

    main_shop1_3 = main_shops[1:3]

    main_shop3_7 = main_shops[3:7]

    main_shop7_11 = main_shops[7:11]

    main_shows = Mainshow.objects.all()

    data= {
        "title": "首页",
        "main_wheels": main_wheels,
        "main_navs": main_navs,
        "main_must_buys": main_mustbuys,
        'main_shop0_1': main_shop0_1,
        'main_shop1_3': main_shop1_3,
        'main_shop3_7': main_shop3_7,
        'main_shop7_11': main_shop7_11,
        'main_shows': main_shows,


    }
    return render(request, 'main/home.html',context=data)


def market(request):
    return redirect(reverse('shoppingsite:market_with_params', kwargs={
        "typeid": 104749,
        "childcid":0,
        'order_rule': 0,
    }))


def market_with_params(request, typeid, childcid, order_rule):

    foodtypes = FoodType.objects.all()
    good_list = Goods.objects.filter(categoryid=typeid)

    if childcid == ALL_TYPE:
        pass
    else:
        good_list = good_list.filter(childcid=childcid)

    if order_rule == ORDER_TOTAL:
        pass
    elif order_rule == ORDER_PRICE_UP:
        good_list = good_list.order_by("price")
    elif order_rule == ORDER_PRICE_DOWN:
        good_list = good_list.order_by("-price")
    elif order_rule == ORDER_SALE_UP:
        pass
    elif order_rule == ORDER_SALE_DOWN:
        pass



    foodtype = foodtypes.get(typeid=typeid)


    foodtypechildnames = foodtype.childtypenames
    foodtypechildname_list = foodtypechildnames.split("#")
    foodtype_childname_list = []

    for foodtypechildname in foodtypechildname_list:
        foodtype_childname_list.append(foodtypechildname.split(":"))
    order_rule_list = [
        ['综合排序', ORDER_TOTAL],
        ['价格升序', ORDER_PRICE_UP],
        ['价格降序', ORDER_PRICE_DOWN],
    ]
    data = {
        "title": "闪购",
        "foodtypes": foodtypes,
        "goods_list": good_list,
        "typeid": int(typeid),
        "foodtype_childname_list": foodtype_childname_list,
        "childcid":childcid,
        'order_rule_list':order_rule_list,
        'order_rule_view':order_rule,
    }
    return render(request, 'main/market.html', context=data)


def cart(request):
    return render(request, "main/cart.html")


def mine(request):
    user_id = request.session.get('user_id')

    data = {
        'title':'我的',
        'is_login': False,
    }

    if user_id:
        user = AAAUser.objects.get(pk=user_id)
        data['is_login'] = True
        data['username'] = user.u_username
        data['icon'] = MEDIA_KEY_PREFIX + user.u_icon.url

    return render(request, "main/mine.html", context=data)


def register(request):
    if request.method == "GET":

        data = {
            "title": "注册",
        }

        return render(request, 'user/register.html', context=data)
    elif request.method == 'POST':

        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        icon = request.FILES.get("icon")

        password = make_password(password)

        user = AAAUser()
        user.u_username = username
        user.u_password = password
        user.u_email = email
        user.u_icon = icon

        user.save()

        return redirect(reverse("shoppingsite:login"))


def login(request):

    if request.method == "GET":
        data = {
            "title": "登录",
        }
        return render(request, 'user/login.html', data)
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        users = AAAUser.objects.filter(u_username=username)
        if users.exists():
            user  = users.first()
            if check_password(password, user.u_password):

                request.session['user_id'] = user.id

                return redirect(reverse('shoppingsite:mine'))
            else:
                print('password wrong')
                return redirect(reverse('shoppingsite:login'))
        print('user not exist')
        return redirect(reverse('shoppingsite:login'))


def check_user(request):
    username = request.GET.get("username")
    users = AAAUser.objects.filter(u_username=username)

    data = {
        "status": HTTP_OK,
        "msg": 'valid username',
    }

    if users.exists():
        data['status'] = HTTP_USER_EXIST
        data['msg'] = 'user already exists'
    else:
        pass

    return JsonResponse(data=data)


def check_email(request):
    email = request.GET.get("email")
    emails = AAAUser.objects.filter(u_email=email)

    data = {
        "status":HTTP_OK,
        "msg": 'valid_email',
    }

    if emails.exists():
        data['status'] = HTTP_EMAIL_EXIST
        data['msg'] = 'email already existis'
    else:
        pass

    return JsonResponse(data=data)


def logout(request):
    request.session.flush()

    return redirect(reverse('shoppingsite:mine'))


def send_email(request):
    subject = 'aaa activate'
    message = "<h1>do you miss me</h1>"
    from_email = "qfhjack@gmail.com"
    recipient_list = ['sharonzhao83@gmail.com','fahaoq@mtu.edu']


    send_mail(subject, message=message, html_message=message, from_email=from_email, recipient_list=recipient_list)
    return HttpResponse("send success")