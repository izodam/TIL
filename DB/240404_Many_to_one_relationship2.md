### User와 다른 모델 간의 모델 관계 설정

1. User & Article
   Article(N) - User(1) : 0개 이상의 게시글은 1명의 회원에 의해 작성될 수 있다.
2. User & Comment
   Comment(N) - User(1) : 0개 이상 댓글은 1명의 회원에 의해 작성 될 수 있다.

## Article & User

### 모델 관계 설정

user 외래 키 정의

```python
from django.conf import settings

class Article(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	...
```

- User 모델을 참조하는 2가지 방법
  - django 프로젝트 '내부적인 구동 순서'와 '반환값'에 따른 이유
  - **User 모델은 직접 참조하지 않음!!**

|               |       `get_user_model()`        |  `settings.AUTH_USER_MODEL`   |
| :-----------: | :-----------------------------: | :---------------------------: |
|    반환 값    |      User Object<br>(객체)      | 'accountss.User' <br>(문자열) |
| **사용 위치** | models.py가 아닌 다른 모든 위치 |           models.py           |

- Migration
  ![](./asset/Pasted%20image%2020240404091743.png)
  - 기존에 테이블이 있는 상황에서 필드를 추가 하려하기 때문에 발생하는 과정
  - 기본적으로 모든 필드에는 NOT NULL 제약조건이 있기 때문에 데이터 없이는 새로운 필드가 추되지 못함.
  - '1'을 입력하고 Enter 진행
    ![](./asset/Pasted%20image%2020240404091801.png)
  - 추가하는 외래 키 필드에 어떤 데이터를 넣을것인지 직접 입력해야 함
  - 마찬가지로 '1'을 입력하고 Enter 진행
    -> 기존에 작성된 게시글이 있다면 모두 1번 회원이 작성한 것으로 처리 됨
  - 이후로 migrate 진행

### 게시글 CREATE

기존 ArticleForm 출력 변화 확인
User 모델에 대한 외래 키 데이터 입력을 받기 위해 불필요한 input이 출력

- ArticleForm 출력 필드 수정

```python
# articles/forms.py
class ArticleForm(forms.ModelForm):
	class Meta
		model = Article
		fields = ('title', 'content',)
```

- 게시글 작성 시 작성자 정보가 함께 저장될 수 있도록 save의 commit 옵션 활용

```python
# articles/views.py

@login_required
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)
```

### 게시글 READ

- 각 게시글 작성자 이름 출력

```html
<!-- articles/index.html -->

{% for article in articles %}
    <p>작성자: {{ article.user }}</p>
    <p>글 번호: {{ article.pk }}</p>
    <a href="{% url "articles:detail" article.pk %}">
      <p>글 제목: {{ article.title }}</p>
    </a>
    <p>글 내용: {{ article.content }}</p>
    <hr>
  {% endfor %}
```

```html
<!-- articles/detail.html -->

<h1>Detail</h1>
 
<h2>{{ article.pk }} 번째 글</h2>
 
<hr />
<p>작성자: {{ article.user }}</p>
<p>제목: {{ article.title }}</p>
<p>내용: {{ article.content }}</p>
<p>작성일: {{ article.created_at }}</p>
<p>수정일: {{ article.updated_at }}</p>
```

### 게시글 UPDATE

- 본인의 게시글만 수정 할 수 있도록 하기

```python
# articles/views.py

@login_required
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user == article.user:
	    if request.method == 'POST':
	        form = ArticleForm(request.POST, instance=article)
	        if form.is_valid():
	            form.save()
	            return redirect('articles:detail', article.pk)
	    else:
	        form = ArticleForm(instance=article)
	else:
		return redirect('articles:index')
    context = {
        'form': form,
        'article': article,
    }
    return render(request, 'articles/update.html', context)
```

- 작성자가 아니라면 수정/삭제 버튼을 출력하지 않도록 하기

```html
<!-- articles/detail.html -->

{% if request.user == article.user %}
  <a href="{% url "articles:update" article.pk %}">UPDATE</a>
  <form action="{% url "articles:delete" article.pk %}" method="POST">
    {% csrf_token %}
    <input type="submit" value="DELETE">
  </form>
{% endif %}
```

### 게시글 DELETE

- 본인의 게시글만 삭제할 수 있도록 하기

```python
# articles/views.py

@login_required
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user == article.user:
      article.delete()
    return redirect('articles:index')
```

## Comment & User

### 모델 관계 설정

- user 외래 키 정의

```python
# articles/models.py

class Comment(models.Model):
	article = models.ForignKey(Article, on_delete=models.CASCADE)
	user = models.ForignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	...
```

- Migration
  - Article와 User 모델 관계 설정 때와 동일한 상황으로
  - 같은 방법으로 해결하면 됨

### 댓글 CREATE

- 댓글 작성 시 작성자 정보가 함께 저장할 수 있도록 작성

```python
# articles/views.py

def comments_create(request, pk):
    article = Article.objects.get(pk=pk)
    comments = article.comment_set.all()
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.user = request.user
        comment.save()
        return redirect('articles:detail', article.pk)
    context = {
        'comment_form': comment_form,
        'article': article,
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)
```

### 댓글 READ

- 댓글 출력 시 댓글 작성자와 함게 출력

```html
<!-- articles/detail.html -->

{% for comment in comments %}
<li>{{ comment.user }} - {{ comment.content }} ...</li>
{% endfor %}
```

### 댓글 DELETE

- 본인의 댓글만 삭제할 수 있도록 하기

```python
# articles/views.py

def comments_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.user == comment.user
	    comment.delete()
    return redirect('articles:detail', article_pk)
```

- 해당 댓글의 작성자가 아니라면, 댓글 삭제 버튼을 출력하지 않도록 함

```html
<!-- articles/detail.html -->

<ul>
	{% for comment in comments %}
		<li>
			{{ comment.user }} - {{ comment.content }}
			{% if request.user == comment.user %}
				<form action="{% url "articles:comments_delete" article.pk comment.pk %}" method="POST" style="display: inline;">
					{% csrf_token %}
					<input type="submit" value="삭제">
				</form>
			{% endif %}
		</li>
	{% endfor %}
</ul>
```
