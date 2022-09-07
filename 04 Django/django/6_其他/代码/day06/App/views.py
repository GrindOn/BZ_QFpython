from captcha.helpers import captcha_image_url
from captcha.models import CaptchaStore
from django.contrib.auth.hashers import make_password, check_password
from django.core.mail import send_mail, send_mass_mail, EmailMultiAlternatives
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader

from App.forms import LoginForm
from day06.settings import EMAIL_HOST_USER, EMAIL_FROM


def handle_captcha(request):
    if request.method == "POST":
        form = LoginForm(request.POST,request)
        print(form)
        if form.is_valid():
            print("验证通过")
            return HttpResponse("验证通过")
        else:
            return render(request, 'app/verifycode.html', locals())
    else:
        form = LoginForm()
        return render(request,'app/verifycode.html',locals())


def mail_send(request):
    # 发送一封邮件
    # res = send_mail('习近平回信勉励北京大学援鄂医疗队全体','习近平指出，青年一代有理想、有本领、有担当，国家就有前途',EMAIL_FROM,
    #                 ['landmark_csl@126.com','y1570069809@163.com'])

    # 发送多封邮件
    # message1 = ('习近平回信勉励北京大学', '<b>近平指出，青年一代有理想</b>', EMAIL_FROM, ['landmark_csl@126.com','y1570069809@163.com'])
    # message2 = ('习近平回信勉励北京大学', '<b>近平指出，青年一代有理想</b>', EMAIL_FROM, ['landmark_csl@126.com','y1570069809@163.com'])
    # send_mass_mail((message1, message2), fail_silently=False)

    # html格式邮件
    html_content = loader.get_template('active.html').render({'username': '小花猫'})
    msg = EmailMultiAlternatives('习近平回信勉励北京大学', from_email=EMAIL_FROM, to=['landmark_csl@126.com'])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    return HttpResponse("邮件发送")


def refresh(request):
    new_key = CaptchaStore.pick()
    res = captcha_image_url(new_key)
    print(new_key)
    print(res)
    return HttpResponse(res)

def test_pass(request):

    password = make_password("123")
    print(check_password('123',password))
    return HttpResponse("ok")

# 不使用表单
def output_yzm(request):
    if request.method == "POST":
        print(request.POST)
        yzm = request.POST.get('yzm','')
        hashkey = request.POST.get('code')
        # 根据key获取验证码对象
        cap = CaptchaStore.objects.filter(hashkey=hashkey).first()
        if cap:#存在
            if cap.response == yzm.lower():
                return HttpResponse("验证成功")
        return HttpResponse("验证失败")
    else:
        # 生成hashkey和image_url
        new_key = CaptchaStore.pick()
        image_url = captcha_image_url(new_key)

        return render(request,'app/vc.html',locals())