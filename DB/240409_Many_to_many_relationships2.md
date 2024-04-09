## 팔로우 기능 구현
### 프로필
1. url 작성
```python
# accounts/urls.py

urlpatterns = [
	...
    path('profile/<username>/', views.profile, name='profile'),
]
```
2. view 함수 작성
```python
# accounts/views.py

from django.contrib.auth import get_user_model

def profile(request, username):
    User = get_user_model()
    person = User.objects.get(username=username)
    context = {
        'person': person
    }
    return render(request, 'accounts/profile.html', context)
```
3. profile 템풀릿 작성
```html
<!-- accounts/profile.html -->

<h1>{{ person.username }}님의 프로필</h1>
<hr />

<h2>{{ person.username }}가 작성한 게시글</h2>
{% for article in person.article_set.all %}
<div>{{ article.title }}</div>
{% endfor %}

<hr />

<h2>{{ person.username }}가 작성한 댓글</h2>
{% for comment in person.comment_set.all %}
<div>{{ comment.content }}</div>
{% endfor %}

<hr />

<h2>{{ person.username }}가 좋아요한 게시글</h2>
{% for article in person.like_articles.all %}
<div>{{ article.title }}</div>
{% endfor %}
```
4. 프로필 페이지로 이동할 수 있는 링크 작성
```html
<!-- articles/index.html -->

<a href="{% url "accounts:profile" user.username %}">내 프로필</a>
  
<p>작성자 : <a href="{% url "accounts:profile" user.username %}">{{ article.user }}</a></p>

```

### 기능 구현
User(M) - User(N)
회원은 0명 이상의 팔로워를 가질 수 있고, 0명 이상의 다른 회원들을 팔로잉 할 수 있음
1. ManyToManyField 작성
```python
# accounts/models.py

class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
```
- 참조
	- 내가 팔로우하는 사람들(팔로잉)
- 역참조
	- 상대방 입장에서 나는 팔로워 중 한 명(팔로워)
2. migrate 진행
3. url 작성
```python
# accounts/urls.py

urlpatterns = [
	...
    path('<int:user_pk>/follow/', views.follow, name='follow'),
]
```
4. view 함수 작성
```python
# accounts/views.py

@login_required
def follow(request, user_pk):
    User = get_user_model()
    person = User.objects.get(pk=user_pk)
    if person != request.user:
        if request.user in person.followers.all():
            person.followers.remove(request.user)
        else:
            person.followers.add(request.user)
    return redirect('accounts:profile', person.username)
```
5. 프로필 유저의 팔로잉, 팔로워 수 & 팔로우, 언팔로우 버튼 작성
```html
<!-- accounts/profile.html -->

<h1>{{ person.username }}님의 프로필</h1>
<div>
	팔로잉 : {{ person.followings.all|length}} / 팔로워 : {{ person.followers.all|length }}
</div>
{% if request.user != person %}
<div>
	<form action="{% url "accounts:follow" person.pk %}" method="POST">
		{% csrf_token %}
		{% if request.user in person.followers.all %}
		<input type="submit" value="언팔로우">
		{% else %}
		<input type="submit" value="팔로우">
		{% endif %}
	</form>
</div>
{% endif %}
<hr />
```


### 참고
- `.exists()`
	- QuerySet에 결과가 포함되어 있으면 True를 반환하고 결과가 포함되어 있지 않으면 False를 반환
	- 큰 QuerySet에 있는 특정 객체 검색에 유용
	- 적용 전
	```python
	# articles/views.py

	@login_required
	def likes(request, article_pk):
	    article = Article.objects.get(pk=article_pk)
	    if request.user in article.like_users.all():
	        article.like_users.remove(request.user)
	    else:
	        article.like_users.add(request.user)
	    return redirect('articles:index')
	```
	- 적용 후
	```python
	# articles/views.py

	@login_required
	def likes(request, article_pk):
	    article = Article.objects.get(pk=article_pk)
	    if article.like_users.filter(pk=request.user.pk).exists():
	        article.like_users.remove(request.user)
	    else:
	        article.like_users.add(request.user)
	    return redirect('articles:index')
	```


## Fixtures
Django가 데이터베이스로 가져오는 방법을 알고 있는 데이터 모음
데이터는 데이터베이스 구조에 맞추어 작성 되어있음
- 초기 데이터 제공

### fixtures 활용
- 명령어
	- dumpdata : 생성(데이터 추출)
	- loaddata : 로드 (데이터 입력)

#### dumpdata
데이터베이스의 모든 데이터를 추출
```bash
$ python manage.py dumpdata [app_name[.ModelName] [app_name[.ModelName] ...]] > filename.json
```

```bash
$ python manage.py dumpdata --indent 4 articles.article > articles.json

$ python manage.py dumpdata --indent 4 accounts.user > user.json
$ python manage.py dumpdata --indent 4 articles.comment > comments.json

```

#### loaddata
Fixtures 데이터를 데이터베이스로 불러오기
파일 기본 경로 : app_name/fixtures/
django는 설치된 모든 app의 디렉토리에서 fixtures 폴더 이후 경로로 fixtures 파일을 찾아 load
1. db.sqlite3 파일 삭제 후 migrate 진행
2. load 진행 후 데이터가 잘 입력되었는지 확인
```bash
$ python manage.py loaddata articles.json user.json comments.json
```
- 주의사항
	- loaddata를 한번에 받지 않고 별도로 실행한다면 모델 관계에 따라 load 순서가 중요할 수 있음
	- 즉 현재 모델 관계에서는 user -> article -> comment 순으로 data를 load해야 오류가 발생하지 않음

### 참고
모든 모델 한번에 dump 하기
```bash
$ python manage.py dumpdata --indent 4 articles.article articles.comment accounts.user > data.json

python manage.py dumpdata --indent 4 > data.json
```



## Improve query
같은 결과를 얻기 위해 DB측에 보내는 query 개수를 점차 줄여 조회하기

### annotate
SQL의 GROUP BY를 사용
- 문제 원인 : 각 게시글마다 댓글 개수를 반복 평가
-> 게시글을 조회하면서 **댓글 개수까지 한번에 조회**해서 가져오기
```python
# views.py

def index_1(request):
	articles = Article.objects.annotate(Count('comment')).order_by('-pk')
	context = {
		"articles": articles,
	}
	return render(request, 'articles/index_1.html', context)
```
```html
<!-- index1.html -->
<p> 댓글개수 : {{article.comment__count}}</p>
```

### select_related
SQL의 INNER JOIN을 사용
1:1 또는 N:1 참조 관계에서 사용
- 문제 원인 : 각 게시글마다 작성한 유저명까지 반복 평가
-> 게시글을 조회하면서 **유저 정보까지 한번에 조회**해서 가져오기
```python
# views.py

def index_2(request):
	articles = Article.objects.select_related('user').order_by('-pk')
	context = {
		'articles' : articles,
	}
	return render(request, 'articles/index_2.html', context)
```

### prefetch_related
Python을 사용한 JOIN을 진행
M:N 또는 N:1 역참조 관계에서 사용
- 문제 원인 : 각 게시글 출력 후 각 게시글의 댓글 목록까지 개별적으로 모두 평가
-> 게시글을 조회하면서 **참조된 댓글까지 한번에 조회**해서 가져오기
```python
# views.py

def index_3(request):
	articles = Article.objects.prefetch_related('comment_set').order_by('-pk')
	context = {
		'articles': articles,
	}
	return render(request, 'articles/index_3.html', context)
```

### select_related & prefetch_related
- 문제 원인 : 게시글 + 각 게시글의 댓글 목록 + 댓글의 작성자 를 단계적으로 평가
-> 게시글을 조회하면서 참조된 댓글까지 한번에 조회
```python
# views.py

  
def index_4(request):
    articles = Article.objects.prefetch_related('comment_set').order_by('-pk')
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index_4.html', context)
```

-> 게시글 + 각 게시글의 댓글 목록 + 댓글의 작성자를 한번에 조회
```python
# views.py

def index_4(request):
     articles = Article.objects.prefetch_related(
         Prefetch('comment_set', queryset=Comment.objects.select_related('user'))
     ).order_by('-pk')
  
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index_4.html', context)
```