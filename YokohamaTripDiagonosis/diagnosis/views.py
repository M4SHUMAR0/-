from django.shortcuts import render

# Create your views here.
def judge_result(request):
    price=request.GET.get("price")
    personality=request.GET.get("personality")
    pace=request.GET.get("pace")
    member=request.GET.get("member")
    return render(request,"templates/diagnosis.html",{"price":price,"personality":personality,"pace":pace,"member":member})