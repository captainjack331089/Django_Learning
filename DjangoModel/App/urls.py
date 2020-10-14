from django.conf.urls import url

from App import views

urlpatterns = [
    url(r'^addpersons/',  views.add_persons),
    url(r'^getpersons/', views.get_persons),
    url(r'^addperson/', views.add_person),
    url(r'^getperson/', views.get_person),
    url(r'^getppl/', views.get_ppl),
]