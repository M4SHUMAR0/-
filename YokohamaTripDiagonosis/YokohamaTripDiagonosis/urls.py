"""YokohamaTripDiagonosis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,re_path
from django.conf.urls import include
from .pages import diagnosis_top,diagnosis,result1,result2,result3,result4

urlpatterns = [
    path('admin/', admin.site.urls),
    path('diagnosis_top/', diagnosis_top.diagnosis_top,name="diagnosis_top"),
    path('diagnosis/', diagnosis.diagnosis,name="diagnosis"),
    path('result1/', result1.result1,name="result1"),
    path('result2/', result2.result2,name="result2"),
    path('result3/', result3.result3,name="result3"),
    path('result4/', result4.result4,name="result4"),
    re_path(r'^diagnosis/', include('diagnosis.urls')),
]
