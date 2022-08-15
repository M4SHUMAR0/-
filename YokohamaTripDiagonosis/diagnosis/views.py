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
    return render(request,"templates/diagnosis.html",{"price":price,"personality":personality,"pace":pace,"member":member})

# def result1(request):
#     return render(request, 'result1.html')

# def result2(request):
#     return render(request, 'result2.html')

# def result3(request):
#     return render(request, 'result3.html')

# def result4(request):
#     return render(request, 'result4.html')

# def judge_result(request):
#     price=request.GET.get("price")
#     personality=request.GET.get("personality")
#     pace=request.GET.get("pace")
#     member=request.GET.get("member")
#     return render(request,"templates/diagnosis.html",{"price":price,"personality":personality,"pace":pace,"member":member})