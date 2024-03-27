실습 url : <br>
[07-django-form](./codes/Django/07-django-form/)

## Django form

사용자 입력 데이터를 수집하고, 처리 및 유효성 검사를 수행하기 위한 도구

- 유효성 검사를 단순화하고 자동화 할 수 있는 기능을 제공
- HTML form의 생성, 데이터 유효성 검사 및 처리를 쉽게 할 수 있도록 도움

- HTML ‘form’
  - 유효한 데이터인지에 대한 확인이 필요

### 유효성 검사

수집한 데이터가 정확하고 유효한지 확인하는 과정

- 유효성 검사를 구현하기 위해서는 입력 값, 형식, 중복, 범위, 보안 등 많은 것들을 고려해야 함
- 이런 과정과 기능을 직접 개발하는 것이 아닌 Django가 제공하는 Form을 사용

## form class

- form class 정의

  - form.py 직접 생성해줘야 합니다!

  ```python
  # articles/forms.py

  from django import forms

  class ArticleForm(forms.Form):
      title = forms.CharField(max_length=10)
      # TextField가 존재하지 않음
      content = forms.CharField()
  ```

- new 과정 변화

  ```python
  # articles/views.py

  from .forms import ArticleForm

  def new(request):
      form = ArticleForm()
      context = {
          'form': form
      }
      return render(request, 'articles/new.html', context)

  ```

  ```Django
  <!-- articles/new.html -->

  <form action="{% url "articles:create" %}" method="POST">
      {% csrf_token %}
      {{ form }}
      <input type="submit">
    </form>
  ```

  - `<input type="text" name="title" maxlength="10" required="" id="id_title">`
    - title이 10자이상 써지지 않는다!!

- form rendering options
  - label, input 쌍을 특정 HTML 태그로 감싸는 옵션
    - as_div도 가능은 합니당

### Widgets

HTML ‘input’ element의 표현을 담당

- 단순히 input 요소의 속성 및 출력되는 부분을 변경하는 것

  ```python
  from django import forms

  class ArticleForm(forms.Form):
      title = forms.CharField(max_length=10)
      content = forms.CharField(widget=forms.Textarea)
  ```

## Django ModelForm

- Form : 사용자 입력 데이터를 DB에 저장하지 않을 때 (ex. 로그인)
- ModelForm : 사용자 입력 데이터를 DB에 저장해야 할 때 (ex. 게시글 작성, 회원가입)

### ModelForm

Model과 연결된 Form을 자동으로 생성해주는 기능을 제공

- form + model
  ```python
  class ArticleForm(forms.ModelForm):
      class Meta:
          model = 어떤 모델과 연동?
          fields = 그 모델에서 어떤 필드를 쓸지
  ```
- meta class

  - ModelForm의 정보를 작성하는 곳
  - model, fields 속성을 필수로 가져야 함

- ‘fields’및 ‘exclude’속성
  - exclude 속성을 사용하여 모델에서 포함하지 않을 필드를 지정할 수도 있음
- 제목 input에 공백을 입력 후 에러 메시지 출력 확인 → 유효성 검사의 결과

  - 무조건 공백이여야 한다
  - 빈칸으로 제출 시 Django에서 막히는 것이 아니라 input 태그의 내부 속성으로 Django에 데이터가 전달되기 전에 오류가 남

- is_valid()

  - 여러 유효성 검사를 실행하고, 데이터가 유효한지 여부를 Boolean으로 반환

- save
  - 생성과 수정을 구분하는 법
    - 키워드 인자 instance 여부를 통해 생성할지, 수정할지 결정

## Handling HTTP requests

### new & create 결합

- new & create view 함수간 공통점과 차이점
  - 공통점 : 데이터 생성을 구현하기 위함
  - 차이점 : new는 GET method 요청만을, create는 POST method 요청만을 처리
- 두 함수를 결합

  - method가 post일때는 create
  - 그게 아니라면 단순히 form 인스턴스 생성

- 기존 new 관련 코드 수정
  - url - new 제거
  - new url을 create url로 변경

### edit & update 결합

new create 결합과 비슷하게 if/else구문으로 결합함
