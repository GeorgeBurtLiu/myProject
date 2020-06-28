from django.http import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.
def login_view(request):
    return render(request, 'login.html')


def login(request):
    # 接受请求参数
    uname = request.POST.get('uname', '')
    pwd = request.POST.get('pwd', '')
    # 判断
    # if uname == 'zhangsan' and pwd == '123':
    #     return HttpResponse('登录成功！')

    if uname and pwd:
        n = Student.objects.filter(sname=uname, spwd=pwd).count()
        if n == 1:
            return HttpResponse('登录成功！')

    return HttpResponse('登录失败！')


def register_view(request):
    if request.method == 'GET':
        return render(request, 'register.html')

    if request.method == 'POST':
        sname = request.POST.get('uname', '')
        spwd = request.POST.get('pwd', '')

        if sname and spwd:
            stu = Student(sname=sname, spwd=spwd)
            stu.save()
            return HttpResponse('注册成功！')
    return HttpResponse('处理注册功能')


def show_view(request):
    stus = Student.objects.all()
    return render(request, 'show.html', {'students': stus})