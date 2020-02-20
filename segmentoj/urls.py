"""segmentoj URL Configuration

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
from django.urls import path, include
from . import views
import problem.views
from . import api

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.welcome),

    # problem

    path('problem/list', problem.views.problemlist),
    path('problem/show/<int:pid>', problem.views.problemshow),

    # user
    path('user/login', views.login),
    path('user/logout', views.logout),
    path('user/register', views.register),

    # api
    path('api/application/user/login', api.login_api),
    path('api/application/user/logout', api.logout_api),
    path('api/application/user/register', api.register_api),
]

if settings.DEBUG:
    urlpatterns += + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
