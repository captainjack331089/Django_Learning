from django.conf.urls import url

from Two import views

urlpatterns = [
    url(r'^hello/', views.hello, name='hello'),

    url(r'^login/', views.login, name='login'),
    url(r'^mine/', views.mine, name='mine'),
    url(r'^logout/', views.logtout, name='logout'),
    url(r'^register/', views.register, name='register'),
    url(r'^studentlogin/', views.student_login, name='student_login'),
    url(r'^studentmine/', views.student_mine, name='student_mine'),
]

app_name = 'two'