from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from App.models import Student


def hello(request):
    return HttpResponse('Hello')


def index(request):
    #本质也是返回httpresponse，它帮我们把模版和数据渲染成字符串
    return render(request, 'index.html')

def get_students(request):
    students = Student.objects.all()
    student_dict = {
        "hobby":"coding",
        "time":"one year",
    }
    code = """
            <h2>睡着了</h2>
            <script type="text/javascript">
               # alert("你的网站被攻陷了！");
                var lis = document.getElementsByTagName("li");
                for (var i=0; i<lis.length; i++){
                    var li = lis[i];
                    li.innerHTML="日本是中国的一部分！";
                }
            </script>
    """

    data = {
        'students': students,
        'student_dict': student_dict,
        'count': 5,
        'code': code,
    }

    return render(request, 'student_list.html', context=data)


def template(request):
    return render(request,'home.html', context={"title": "home"})


def home(request):
    return render(request, 'home_mine.html')

