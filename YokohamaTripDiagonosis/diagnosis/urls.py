from django.urls import re_path
from . import views
 
urlpatterns = [
    re_path(r'^$', views.judge_result, name='judge_result'),
]