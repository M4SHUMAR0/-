from django.shortcuts import render

# Create your views here.
def diagnosis_top(request):
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
    return render(request,"templates/diagnosis.html",{"price":price,"personality":personality,"pace":pace,"member":member,"total":total})

def result1(request):
    return render(request, 'result1.html')

def result2(request):
    return render(request, 'result2.html')

def result3(request):
    return render(request, 'result3.html')

def result4(request):
    return render(request, 'result4.html')

# def judge_result(request):
#     price=request.GET.get("price")
#     personality=request.GET.get("personality")
#     pace=request.GET.get("pace")
#     member=request.GET.get("member")
#     return render(request,"templates/diagnosis.html",{"price":price,"personality":personality,"pace":pace,"member":member})