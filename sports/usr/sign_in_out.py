from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
import json

def signin(request):
    # 从 HTTP POST 请求中获取用户名、密码参数
    request_data = json.loads(request.body)
    userName = request_data["username"]
    passWord = request_data["password"]

    # 使用 Django auth 库里面的 方法校验用户名、密码
    user = authenticate(username=userName, password=passWord)

    # 如果能找到用户，并且密码正确
    if user is not None:
        if user.is_active:
            # 在session中存入用户类型
            login(request, user)
            request.session['usertype'] = 'usr'
            return JsonResponse({'ret': 0})
        else:
            return JsonResponse({'ret': 0, 'msg': '用户已经被禁用'})

    # 否则就是用户名、密码有误
    else:
        return JsonResponse({'ret': 1, 'msg': '用户名或者密码错误'})


# 登出处理
def signout(request):
    # 使用登出方法
    logout(request)
    return JsonResponse({'ret': 0})
