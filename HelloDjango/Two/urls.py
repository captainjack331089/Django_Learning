from django.conf.urls import url

from Two import views

urlpatterns = [
    url('index/', views.index),
    url('addstudent/', views.add_student),
    url('getstudent/', views.get_student),
    url('updatestudent/', views.update_student),
    url('deletestudent/', views.delete_student),
]