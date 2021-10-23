from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.http import Http404

# Create your views here.
def index(request):
    today = datetime.today().date()
    # print(today)

    context = {"date":today}

    return render(request, 'foods/index.html', context=context)


def food_detail(request,food):
    context = dict()
    if food == "chicken":
        context["name"] = "닭강정"
        context["description"] = "칼로리 : 매우높음 \t 가격 : 20000만원 미만"
        context["img_path"] = "foods/images/chicken.jpg"

    else:
        raise Http404("잘못된 접근 입니다!")
    
    return render(request, 'foods/detail.html', context=context)