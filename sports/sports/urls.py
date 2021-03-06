"""sports URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import url, include
from django.views.generic import TemplateView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, routers
from splatform import views_news 

# 自动产生接口文档
schema_view = get_schema_view(
    openapi.Info(
        title="HelloDjango REST framework tutorial API",
        default_version="v1",
        description="HelloDjango REST framework tutorial AP",
        terms_of_service="",
        contact=openapi.Contact(email="2535367985@qq.com"),
        license=openapi.License(name="GPLv3 License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny, ),
)

urlpatterns = [
    path('admin/', admin.site.urls), # 管理员
    path('', TemplateView.as_view(template_name='index.html')), # vue主页

    path('home/', TemplateView.as_view(template_name='home.html')), # 赛事主页
    path('login/', TemplateView.as_view(template_name='login.html')), # 赛事主页
    path('talk/', include('boards.urls')), # 讨论区页面
    path('user/', TemplateView.as_view(template_name='user.html')), # 赛事主页
    path('matchinfo/',include('matchinfo.urls')), # 赛事信息页
    path('news/',TemplateView.as_view(template_name='news.html') ), # 赛事新闻区页面
    path('news/detail/', views_news.news_list), # 赛事新闻区子页面
    path('api/mgr/', include('mgr.urls')), # 登录登出
    path('api/usr/', include('usr.urls')), # 注册登录登出
    url('api/info/', include('splatform.urls')), # 数据榜单

    # 接口文档
    re_path(
        r"swagger(?P<format>\.json|\.yaml)",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/",
         schema_view.with_ui("redoc", cache_timeout=0),
         name="schema-redoc"),

]
