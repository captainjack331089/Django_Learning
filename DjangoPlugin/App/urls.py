from django.conf.urls import url

from App import views

urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^editblog/', views.edit_blog, name='edit_blog'),
]

app_name = 'app'