from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    #return HttpResponse("Hello Django!")
    return render(request,"index.html")
#登录动作
def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        if username == 'admin' and password == 'admin123':
            return HttpResponse('登录成功')
        else:
            return render(request,'index.html'),{'error':'username or password error!'}
