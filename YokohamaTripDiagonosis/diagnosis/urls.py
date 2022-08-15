from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.diagnosis_top, name="diagnosis_top"),
    path('diagnosis/',views.diagnosis,name="diagnosis"),
    path('result1/',views.result1,name="result1"),
    path('result2/',views.result2,name="result2"),
    path('result3/',views.result3,name="result3"),
    path('result4',views.result4,name="result4"),   
    path('result/',views.result,name="result"), 
]

# 全体の方
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('diagnosis_top/', diagnosis_top.diagnosis_top,name="diagnosis_top"),
#     path('diagnosis/', diagnosis.diagnosis,name="diagnosis"),
#     path('result1/', result1.result1,name="result1"),
#     path('result2/', result2.result2,name="result2"),
#     path('result3/', result3.result3,name="result3"),
#     path('result4/', result4.result4,name="result4"),
# ]