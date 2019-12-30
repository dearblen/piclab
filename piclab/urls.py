"""piclab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from home import views as home_views
from login import views as login_views
from django.conf.urls import url,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('home/', home_views.home),
    path('home/test_ajax/', home_views.test_ajax),
    path('document/', home_views.document),
    path('admin/', admin.site.urls),
    path('', login_views.login),
    path('index/', login_views.index),
    path('login/', login_views.login),
    path('register/', login_views.register),
    path('logout/', login_views.logout),
    path('captcha/', include('captcha.urls')),
    path('confirm/', login_views.user_confirm),
]+ static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)

