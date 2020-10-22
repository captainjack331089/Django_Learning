from django.db import models

class Main(models.Model):
    img = models.CharField(max_length=512)
    name = models.CharField(max_length=64)
    trackid = models.IntegerField(default=1)

    class Meta:
        abstract = True

class MainWheel(Main):
    """
    aaa_wheel(img,  name,trackid)
    """
    class Meta:
        db_table  = 'aaa_wheel'

class MainNav(Main):
    """
    aaa_nav(img,name,trackid)
    """
    class Meta:
        db_table  = 'aaa_nav'

class MainMustBuy(Main):
    """
    aaa_mustbuy(img, name, trackid)
    """
    class Meta:
        db_table = 'aaa_mustbuy'