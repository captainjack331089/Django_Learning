from django.db import models

# Create your models here.
class User(models.Model):
    objects = models.Manager()
    u_name = models.CharField(max_length=16, unique=True)
    u_password = models.CharField(max_length=256)

class Order(models.Model):
    objects = models.Manager()
    o_num = models.CharField(max_length=16, unique=True)
    o_time = models.DateTimeField(auto_now=True)

class Grade(models.Model):
    objects = models.Manager()
    g_name = models.CharField(max_length=16)

class Student(models.Model):
    objects = models.Manager()
    s_name  = models.CharField(max_length=16)
    s_grade = models.ForeignKey(Grade, on_delete=models.CASCADE)

class Customer(models.Model):
    objects = models.Manager()
    c_name = models.CharField(max_length=16)
    c_cost = models.IntegerField(default=10)

class Company(models.Model):
    object = models.Manager()
    c_name = models.CharField(max_length=16)
    c_girl_num = models.IntegerField(default=10)
    c_boy_num = models.IntegerField(default=7)

class animaManager(models.Manager):
    def get_queryset(self):
        return super(animaManager, self).get_queryset().filter(is_delete=False)
    def create_animal(self, a_name="Chicken"):
        a = self.model()
        a.a_name = a_name

        return a

class Animal(models.Model):

    is_delete = models.BooleanField(default=False)
    a_name = models.CharField(max_length=16)
    #objects = animaManager()
