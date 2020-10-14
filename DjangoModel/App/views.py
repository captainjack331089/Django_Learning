import random

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from App.models import Person


def add_persons(request):
    for i in range(15):
        person = Person()
        flag = random.randrange(100)
        person.p_name = "Tom%d" % i
        person.p_age = flag
        person.p_sex = flag % 2
        person.save()
    return HttpResponse("批量创建成功")


def get_persons(request):
    # persons = Person.objects.filter(p_age__gt=50).filter(p_age__lt=80)
    persons = Person.objects.exclude(p_age__lt=50)
    print(type(persons))
    context = {
        "persons": persons,
    }
    return render(request, 'person_list.html', context=context)

def add_person(request):
    # person = Person.objects.create(p_name="jack", p_age=30, p_sex=False)
    # person = Person(p_name='Rose',  p_age=20, p_sex=False)
    person = Person.create('Sharon')
    person.save()
    return HttpResponse("Jack create success")

def get_person(request):
    persons = Person.objects.all().order_by("p_age")
    persons_values = persons.values()
    print(type(persons_values))
    print(persons_values)

    for person_value in persons_values:
        print(person_value)
    context = {
        "persons": persons
    }
    return render(request, "person_list.html", context=context)


def get_ppl(request):
    # person = Person.objects.get(p_age=56)
    # print(person)
    person = Person.objects.all().first()
    print(person.p_name)
    person_one = Person.objects.all().last()
    print(person_one.p_name)
    return HttpResponse('Get Success')