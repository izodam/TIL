## Many to one relationships

N:1 or 1:N
한 테이블의 0개 이상의 레코드가 다른 테이블의 레코드 한 개와 관련된 관계

- comment(N) - Article(1)
  - 0개 이상의 댓글은 1개의 게시글에 작성될 수 있다.

### ForeignKey()

N:1 관계 설정 모델 필드

- 댓글 모델 정의
  ```python
  # articles/models.py
  class Comment(models.Model):
  	article = models.ForeignKey(Article, on_delete=models.CASCADE)
  ```
  - ForeignKey 클래스의 인스턴스 이름은 **참조하는 모델 클래스 이름의 단수형**으로 작성하는 것을 권장
  - 외래 키는 ForeignKey 클래스를 작성하는 위치와 관계없이 테이블 필드 마지막에 생성
- ForignKey(to, on_delete)
  - to : 참조하는 모델 class 이름
  - on_delete : 외래 키가 참조하는 객체(1)가 사라졌을 때, 외래 키를 가진 객체(N)을 어떻게 처리할 지를 정의하는 설정 (데이터 무결성)
  - on_delete의 CASCADE : 부모 객체(참조 된 객체)가 삭제 됐을 때 이를 참조하는 객체도 삭제
- Migration 이후 댓글 테이블 확인
  - 댓글 테이블의 article_id필드 확인
  - 참조 대상 클래스 이름 + \_ + 클래스 이름
    -> 참조하는 클래스 이름의 소문자(단수형)으로 작성하는 것이 권장되었던 이유

### 댓글 생성 연습

1. shell_plus 실행 및 게시글 작성
   `$ python manage.py shell_plus`
   ```python
   # 게시글 생성
   Article.objects.create(title='title', content='content')
   ```
2. 댓글 생성

   ```python
   # comment 클래스의 인스턴스 comment 생성
   comment = Comment()

   # 인스턴스 변수 저장
   comment.content = 'first commnet'

   # DB에 댓글 저장
   comment.save()

   # 에러 발생
   IntegrityError: NOT NULL constraint failed: articles_comment.article_id
   # articles_commnet 테이블의 ForeignKeyField, article_id 값이 저장 시 누락 되었기 때문
   ```

3. shell_plus 실행 및 게시글 작성

   ```python
   # 게시글 조회
   article = Article.objects.get(pk=1)

   # 외래 키 데이터 입력
   comment.article = article
   # 또는 comment.article_id = article.pk 처럼 pk 값을 직접 외래 키 컬럼에 넣어 줄 수도 있지만 권장하지 않음

   # 댓글 저장 및 확인
   commnet.save()
   ```

4. comment 인스턴스를 통한 article 값 참조하기

   ```python
   comment.pk
   => 1

   comment.content
   => 'first comment'

   # 클래스 변수명인 article로 조회 시 해당 참조하는 게시물 객체를 조회할 수 있음
   comment.article
   => <Article: Article object (1)>

   # article_pk는 존재하지 않는 필드이기 때문에 사용 불가
   comment.article_id
   => 1
   ```

5. comment 인스턴스를 통한 article 값 참조하기

   ```python
   # 1번 댓글이 작성된 게시물의 pk 조회
   comment.article.pk
   => 1

   # 1번 댓글이 작성된 게시물의 content 조회
   comment.article.content
   => 'content'
   ```

6. 두번째 댓글 생성

   ```
   comment = Comment(content='second comment', article=article)
   comment.save()

   comment.pk
   => 2

   commnet
   => <Comment: Comment object (2)>

   comment.article.pk
   => 1
   ```

## 관계 모델 참조

### 역참조

N:1 관계에서 1에서 N을 참조하거나 조회하는 것 (1 -> N)
N은 외래 키를 가지고 있어 물리적으로 참조가 가능하지만 1은 N에 대한 참조 방버이 존재하지 않아 별도의 역참조 기능이 필요

- '모델 인스턴스' . 'related manager(역참조 이름)' . 'QuerySet API'
  - ex) `article.commnet_set.all()`
  - 특정 게시글에 작성된 댓글 전체를 조회하는 명령

#### related manager

역참조 시에 사용하는 매니저
'objects' 매니저를 통해 QuerySet API를 사용했던 것처럼 related manager을 통해 QuerySet API를 사용할 수 있게 됨

- 이름 규칙
  - N:1 관계에서 생성되는 Related manager의 이름은 참조하는 '모델명\_set' 이름 규칙으로 만들어짐
  - 특정 댓글의 게시글 참조 (Commnet -> Article)
    `comment.article`
  - 특정 게시글의 댓글 목록 참조 (Article -> Comment)
    `article.comment_set.all()`
- related manager 연습
  - shell_plus 실행 및 1번 게시글 조회
  ```python
  $ pyhton manage.py shell_plus
  article = Article.objects.get(pk=1)
  ```
  - 1번 게시글에 작성된 모든 댓글 조회하기(역참조)
  ```python
  >>> article.comment_set.all()
  <QuerySet [<Commrny: Comment object (1)>,
  <Comment: Comment object (2)>]>
  ```
  - 1번 게시글에 작성된 모든 댓글의 내용 출력
  ```python
  comments = article.comment_set.all()
  for comment in comments:
  	print(comment.content)
  ```

## 댓글 구현

### CREATE

댓글 데이터를 받기 위한 CommentForm

```python
# articles/forms.py
from .models impoort Article, Comment

class CommentForm(forms.ModelForm):
	class Meta:
		models = Comment
		fields = '__all__'
```

deltail 페이지에 렌더링

```python
# articles/views.py
from .forms import ArticleForm, CommentForm

def detail(request, pk):
	article = Article.objects.get(pk=pk)
	context = {
		'article': article,
		'comment_form': comment_form
	}
	return render(request, 'articles/detail.html', context)
```

외래 키 필드 데이터는 사용자로부터 입력 받는 값이 아닌 view함수 내에서 다른 방법으로 전달받아 저장되어야 함

```python
# articles/forms.py
from .models impoort Article, Comment

class CommentForm(forms.ModelForm):
	class Meta:
		models = Comment
		fields = ('content',)
```

댓글의 외래 키 데이터에 필요한 정보가 바로 게시글의 pk 값

```python
# articles.urls.py

urlpatters = [
	...,
	path('<int:pk>/comments/', views.comments_create, name='comments'),
]
```

```html
<!-- articles/detail.html -->
<form action="{% url "articles:comment_create" article.pk %}" method="POST">
  {% csrf_token %}
  {{ comment_form }}
  <input type="submit">
</form>
```

url에서 넘겨받은 pk 인자를 게시글을 조회하는데 사용

```python
# articles/views.py

def comments_create(request, pk):
	article = Article.objects.get(pk=pk)
	comment_form = CommentForm(request.POST)
	if comment_form.is_valid():
		comment_form.save()
		return redirect('articles:detail', article.pk)
	context = {
		'article': article,
		'comment_form': comment_form,
	}
	return render(request, 'articles/detail.html', context)
```

- `save(commit=False)`
  - DB에 저장하지 않고 인스턴스만 반환

```python
# articles/views.py

def comment_create(request, pk):
    article = Article.objects.get(pk=pk)
    comments = article.comment_set.all()
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment_form.save()
        return redirect('articles:detail', article.pk)
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)
```

### READ

전체 댓글 데이터를 조회

```python
# articles/views.py
from .models import Article, Comment

def detail(request, pk):
	article = Article.objects.get(pk=pk)
	comment_form = CommentForm()
	comments = article.comment_set.all()
	context = {
		'article': article,
		'comment_form': comment_form,
		'comments': comments,
	}
	return render(request, 'articles/detail.html', context)
```

전체 댓글 출력 및 확인

```html
<!-- articles/detail.html -->

<h4>댓글 목록</h4>
<ul>
    {% for comment in comments %}    
  <li>{{ comment.content }}</li>
    {% endfor %}
</ul>
```

### DELETE

댓글 삭제 url

```python
# articles.urls.py

urlpatters = [
	...,
	path('<int:article_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),
]
```

view 함수 정의

```python
# articles/views.py
from .models import Article, Comment

def comments_delete(request, article_pk, comment_pk):
	comment = Comment.objects.get(pk=comment_pk)
	comment.delete()
	return redirect('articles:detail', article_pk)
```

댓글 삭제 버튼

```html
<!-- articles/detail.html -->

<ul>
{% for comment in comments %}
	<li>{{ comment.content }}
	<form action="{% url "articles:comment_delete" article.pk comment.pk %}" method='POST'>
		{% csrf_token %}
		<input type="submit" value='DELETE'>
	</form>
	</li>
{% endfor %}
</ul>
```

### 댓글이 없을 경우 대체 콘텐츠 출력

```html
<ul>
  {% for comment in comments %}
    <li>{{ comment.content }}
    <form action="{% url "articles:comment_delete" article.pk comment.pk %}" method='POST'>
      {% csrf_token %}
      <input type="submit" value='DELETE'>
    </form>
    </li>
  {% empty %}
    <p>댓글이 없어요...</p>
  {% endfor %}
</ul>
```

### 댓글 개수 출력하기

- DTL filter 'length' 사용

```django
{{ comments|length }}

{{ article.comment_set.all|length }}
```

- QuerySet API 'count()' 사용

```django
{{ article.commet_set.count }}
```
