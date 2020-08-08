import calendar
import time

from django.views import View

from .models import DakaTime, User
from django.db import connection
from .forms import RegistForm,LoginForm,SelectForm

from django.shortcuts import render,redirect,reverse
import global_var_model as gl
# render是一个模板
from django.http import HttpResponse

from django.db import connection
from clocka import models
# Create your views here.


class RegistView(View):
    def get(self,request):
        form=RegistForm()
        return render(request,'registration.html',context={'form':form})
    def post(self,request):
        form=RegistForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            # 写入数据库
            user=User(username=username,password=password)
            user.save()
            return redirect(r"/login/")
        else:
            errors=form.errors.get_json_data()
            return render(request,'registration.html',{'errors':errors})

class LoginView(View):
    def get(self,request):
        login_form=LoginForm()
        return render(request,'login.html',context={'form':login_form})
    def post(self,request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = User.objects.get(username=username)
            if user.password == password:
                gl.cur=username
                return redirect("/index/")
        return render(request,'login.html')

def index(request):
    return render(request,'index.html')
def index0(request):
    return render(request,'index0.html')

def daka_view(request):
    # # 获取当前时间戳：十位整型数字（int类型）
    now= calendar.timegm(time.gmtime())
    cur=now%86400

    # 2020-04-24 09:50:00
    # 时间戳为
    morning_begin = 6600
    # 2020-04-24 10:10:00
    # 时间戳为
    time2 = 1587694200
    morning_end=7800
    # 2020-04-24 13:50:00
    # 时间戳为
    time3 = 1587707400
    afternoon_begin=21000
    # 2020-04-24 14:10:00
    # 时间戳为
    time4 = 1587708600
    afternoon_end=22200

    # 2020-04-24 16:50:00
    # 时间戳为
    time5 = 1587718200
    night_begin=31800
    # 2020-04-24 17:10:00
    # 时间戳为
    time6 = 1587719400
    night_end=33000

    time_local = time.localtime(now)
    date = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
    # 时间戳是1970-01-01 00:00:00到现在的秒数，一天为86400秒
    # 所以获取第二天的6个时间直接在当前时间+86400
    if cur>morning_begin and cur<morning_end:
        daka_temp()
        return render(request,'dakasuccess.html',{"date": date})
    elif cur>afternoon_begin and cur<afternoon_end:
        daka_temp()
        return render(request, 'dakasuccess.html', {"date": date})
    elif cur>night_begin and cur<night_end:
        daka_temp()
        return render(request, 'dakasuccess.html', {"date": date})
    else:
        return redirect("/dakafail/")


def daka_success(request):
    return render(request,"dakasuccess.html")

def daka_fail(request):
    return render(request,"dakafail.html")

    # return render(request,"daka.html")
def daka_temp():
    dakatime = DakaTime(username=gl.cur)
    dakatime.save()

class SelectView(View):
    def get(self,request):
        select_form=SelectForm()
        return render(request,'select.html',context={'form':select_form})
    def post(self,request):
        select_form = SelectForm(request.POST)
        if select_form.is_valid():
            username = select_form.cleaned_data.get('username')
            temp = DakaTime.objects.filter(username=username)
            result=[]
            for res in temp:
                result.append(res)
            return render(request,'result.html',{"result":result})
        return HttpResponse("查询失败")

def selectRes(request):
    return render(request,'result.html')






# def get_cursor():
#     return connection.cursor()
#
# def index(request):
#     # cursor=connection.cursor()
#     # # 拿到cursor之后就可以操作这个数据库了
#     # cursor.execute("insert into user(id,name) values(NULL,'AChu')")
#     #
#     # cursor.execute("select id,name from user")
#     #
#     # # fetchall返回所有的sql执行结果，fetchone返回一条结果，返回指定特定的sql语句执行结果使用fetchmany(n)，指定几条n就是几
#     # res=cursor.fetchall()
#     # for result in res:
#     #     print(result)
#
#     # cursor = get_cursor()
#     # cursor.execute("select uname,count from user")
#     # user = cursor.fetchall()
#     return render(request, 'index.html')
#
# def login_view(request):
#
#     # 查询用户信息是否在表里面
#     return render(request,'login.html')
#
# def registration_view(request):
#     # if request.method=='GET':
#     #     return render(request, "registration.html")
#     # else:
#     #     uname=request.POST.get('uname')
#     #     password=request.POST.get('password')
#     #     cursor=get_cursor()
#     #     cursor.execute("insert into user(uname,password,count,daka_time) value('%s','%s',null,null)"%(uname,password))
#     # 一个对象对应数据库表中的一条数据
#     if request.method=='GET':
#         return render(request, "registration.html")
#     else:
#         uname=request.POST.get('uname')
#         password=request.POST.get('password')
#         user=User(uname=uname,password=password)
#     # # save方法把对象把存在数据库中
#         user.save()
#         return redirect(reverse('login.html'))
#

