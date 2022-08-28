from django.shortcuts import render
from . import models
# Create your views here.
def diagnosis_top(request):
    if request:
        return render(request, 'diagnosis_top.html')
    else:
        star1=request.GET.get("star1")
        star2=request.GET.get("star2")
        star3=request.GET.get("star3")
        star4=request.GET.get("star4")
        star5=request.GET.get("star5")
        if star5:
            rate=models.evaluation(evaluation=star5)
        elif star4:
            rate=models.evaluation(evaluation=star4)
        elif star3:
            rate=models.evaluation(evaluation=star3)
        elif star2:
            rate=models.evaluation(evaluation=star2)
        elif star1:
            rate=models.evaluation(evaluation=star1)
        else:
            rate=models.evaluation(evaluation=0)
        rate.save()
        return render(request, 'diagnosis_top.html')



def diagnosis(request):
    return render(request, 'diagnosis.html')

def result(request):
    price=request.GET.get("price")
    personality=request.GET.get("personality")
    pace=request.GET.get("pace")
    member=request.GET.get("member")
    if price=="rich":
        grade_price=1
    else:
        grade_price=0
    
    if personality=="outdoor":
        grade_personality=2
    elif personality=="middle":
        grade_personality=1
    else:
        grade_personality=0
    
    if pace=="quick":
        grade_pace=4
    else:
        grade_pace=0
    total=grade_price+grade_personality+grade_pace
    return render(request,"result.html",{"price":price,"personality":personality,"pace":pace,"member":member,"total":total})

# def judge_result(request):
#     price=request.GET.get("price")
#     personality=request.GET.get("personality")
#     pace=request.GET.get("pace")
#     member=request.GET.get("member")
#     return render(request,"templates/diagnosis.html",{"price":price,"personality":personality,"pace":pace,"member":member})