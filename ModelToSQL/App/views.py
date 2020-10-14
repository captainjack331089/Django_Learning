from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from App.models import UserModel


def index(request):
    return render(request, 'index.html')


def upload_file(request):
    if request.method == "GET":
        return render(request, 'upload.html')
    elif request.method ==  "POST":
        icon = request.FILES.get("icon")
        print(type(icon))
        print(icon)
        with open("/Users/captainjack33/Django_Learning/ModelToSQL/static/img/icon.jpg", 'wb') as save_file:
            for part in icon.chunks():
                save_file.write(part)
                save_file.flush()

        return HttpResponse("文件上传成功")


def image_field(request):
    if request.method == 'GET':
        return render(request, 'image_field.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        icon = request.FILES.get('icon')
        user = UserModel()

        user.u_name = username
        user.u_icon = icon

        user.save()

        return HttpResponse('上传成功%d' %user.id)


def mine(request):

    username = request.GET.get('username')
    user = UserModel.objects.get(u_name=username)
    icon_url = "/static/upload/"+user.u_icon.url
    print("/static/upload/"+user.u_icon.url)
    data = {
        "username": username,
        "icon_url": icon_url,
    }
    return render(request, 'mine.html',context=data)