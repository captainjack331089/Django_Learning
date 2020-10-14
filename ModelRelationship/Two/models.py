from django.db import models

# Create your models here.
class Person(models.Model):
    p_name = models.CharField(max_length=16)
    p_age = models.BooleanField(default=False)

class IDCard(models.Model):
    id_num = models.CharField(max_length=18, unique=True, null=True, blank=True)
    id_person = models.OneToOneField(Person,  on_delete=models.CASCADE, null=True, blank=True)


class Customer(models.Model):
    c_name = models.CharField(max_length=16)

class Goods(models.Model):
    g_name = models.CharField(max_length=16)
    g_customer = models.ManyToManyField(Customer)


class Animal(models.Model):
    a_name  = models.CharField(max_length=16)

    class Meta:
        #不会在数据库中生成映射
        abstract = True

class Cat(Animal):
    c_eat = models.CharField(max_length=32)

class Dog(Animal):
    d_legs  = models.IntegerField(default=4)