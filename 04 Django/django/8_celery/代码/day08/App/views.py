from datetime import datetime, timedelta

from django.core.cache import cache
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader
from django.urls import reverse
from django.views.decorators.cache import cache_page



from App.models import User


# 缓存20秒
from App.util import token_confirm
from day08.settings import EMAIL_FROM


@cache_page(20)
def index(request):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    pre_time = datetime.now() - timedelta(days=3)
    pre_time = pre_time.strftime("%Y-%m-%d %H:%M:%S")
    print(current_time,pre_time)
    return render(request,'index.html',locals())


def cache_all1(request):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return HttpResponse(current_time)


def cache_data1(request):
    # 首先判断数据是否在缓存中，如果在直接获取
    users = cache.get('all_users')


    if not users:  # 如果不在缓存,查询数据库，将结果写入缓存
        users = User.objects.all()
        # cache可以直接把查询结果序列化
        cache.set('all_users',users)
        print("数据库")
    print(users)
    return render(request,'index1.html',locals())


def check_user(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # 检测用户是否存在
        user = User.objects.filter(username=username,password=password).first()
        if user:
            return HttpResponse("用户已经存在")
        # 保存用户信息
        # 刚注册的用户是未激活
        user = User.objects.create(username=username,password=password,is_active=0)

        # 发送邮件，确认激活
        token = token_confirm.generate_validate_token(user.uid)
        print(token)
        # 构造验证url
        url = "http://"+request.get_host()+reverse("App:activeuser",kwargs={'token':token})
        # 加载模板
        html = loader.get_template('active.html').render({'url':url})
        print(url)
        send_mail("账号激活",'',EMAIL_FROM,['landmark_csl@126.com'],html_message=html)
        return HttpResponse("激活邮件已经发送，请登录邮箱确认激活")
    return render(request,'register.html')


def active_user(request,token):
    # 激活用户
    try:
        uid = token_confirm.confirm_validate_token(token)
    except Exception as e:
        print(e)
        try:
            uid = token_confirm.remove_validate_token(token)
            user = User.objects.get(pk=uid)
            user.delete()
        except:
            pass
        return HttpResponse("激活失败，请重新注册")
    try:
        user = User.objects.get(pk=uid)
    except User.DoesNotExist:
        return HttpResponse("你激活的用户不存在，请重新注册")
    user.is_active = 1  # 激活用户
    user.save()

    return HttpResponse("用户已激活，请登录系统")


def exec_tasks(request):
    from App.tasks import hello_world,mail_send,sum_even
    # hello_world.delay(4)  # 把任务添加到任务队列
    # subject, message, from_email, recipient_list
    # mail_send.delay({
    #     'subject':'no zuo no die',
    #     'message':'不作不死',
    #     'recipient_list':['landmark_csl@126.com']
    # })
    #异步获取任务结果
    sum_even.delay(100)
    return HttpResponse("celery")


def handle_log(request):
    print(1 / 0)
    return HttpResponse("日志")