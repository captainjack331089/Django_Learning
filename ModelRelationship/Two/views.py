from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from Two.models import Person, IDCard, Customer, Goods, Cat, Dog


def hello(request):
    return HttpResponse('Two,hello')


def add_person(request):

    username = request.GET.get('username')
    person = Person()
    person.p_name = username
    person.save()

    return HttpResponse('Person 创建成功 %d' % person.id)


def add_idcard(request):

    id_num = request.GET.get("id_num")
    idcard = IDCard()
    idcard.id_num = id_num
    idcard.save()
    return HttpResponse('IDCard %d' % idcard.id)


def band_card(request):

    person = Person.objects.last()
    idcard = IDCard.objects.last()
    idcard.id_person  = person
    idcard.save()
    return HttpResponse('绑定成功')


def remove_person(request):

    person  = Person.objects.last()
    person.delete()

    return HttpResponse('people delete success')


def remove_idcard(request):

    idcard = IDCard.objects.last()
    idcard.delete()

    return HttpResponse('ID Card  remove success')


def get_person(request):

    idcard= IDCard.objects.last()
    person = idcard.id_person

    return HttpResponse(person.p_name)


def get_idcard(request):

    person = Person.objects.last()
    idcard = person.idcard
    return HttpResponse(idcard.id_num)


def add_customer(request):

    c_name = request.GET.get('c_name')
    customer = Customer()
    customer.c_name = c_name
    customer.save()

    return HttpResponse('创建消费者成功 %d' %customer.id)

def add_goods(request):

    g_name = request.GET.get('g_name')
    goods = Goods()
    goods.g_name = g_name
    goods.save()

    return HttpResponse('创建商品成功 %d' %goods.id)


def add_to_cart(request):

    customer  = Customer.objects.last()
    goods = Goods.objects.last()
    # print(type(goods.g_customer))
    # print(goods.g_customer)

    # goods.g_customer.add(customer)
    customer.goods_set.add(goods)
    return HttpResponse("add success")


def get_goods_list(request, customerid):
    customer = Customer.objects.get(pk=customerid)
    goods_list = customer.goods_set.all()
    return render(request, 'goods_list.html', context=locals())


def add_cat(request):

    cat =   Cat()
    cat.a_name = 'Tom'
    cat.c_eat = 'fish'
    cat.save()
    return HttpResponse('Cat create success %d' %cat.id)

def add_dog(request):

    dog =  Dog()
    dog.a_name = 'bobby'

    dog.save()
    return HttpResponse('Dog create success %d' %dog.id)

