import random
from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
        'name' : 'Alice',
    }
    return render(request, 'articles/index.html',context)


def dinner(request):
    foods = [
        '국밥',
        '국수',
        '카레',
        '탕수육',
    ]
    picked = random.choice(foods)
    context = {
        'foods' : foods,
        'picked': picked,
    }
    return render(request, 'articles/dinner.html', context)


def search(request):
    return render(request, 'articles/search.html')


def throw(request):
    return render(request, 'articles/throw.html')

def catch(request):
    # throw 페이지에서 데이터를 받고
    # 그 안에서 사용자 입력 데이터를 추출
    # 템플릿에 그대로 출력
    message = request.GET.get('message')
    context = {
        'massage' : message,
    }
    return render(request,'articles/catch.html', context)

def greeting(request, name):
    context = {
        'name':name,
    }
    return render(request,'articles/greeting.html', context)
