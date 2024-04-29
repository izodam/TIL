from django.shortcuts import render

# Create your views here.
# 메인 페이지를 만드는 index라는 이름의 함수를 작성
# 매개변수를 다른 것을 써도 되지만 암묵적인 룰로 request를 사용함
def index(request):
    # render(요청 객체, 템플릿 경로)
    # 템플릿 경로는 templates 뒤에 경로만 쓰면 된다.
    # 그렇게 약속했기 때문에 templates 폴더명이 지정되어 있는 것
    # render 쓰는 목적 : 페이지 하나 포장할려고
    return render(request, 'articles/index.html')