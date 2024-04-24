## Ajax with follow

### 비동기 팔로우 구현

#### Ajax 적용

1. 프로필 페이지에 axios CDN 작성
2. form 요소 선택을 위해 id 속성 지정 및 선택, action과 method 속성은 삭제

```html
<!-- accounts/profile.html -->
<form id="follow-form">...</form>

<script>
  const formTag = document.querySelector("#follow-form");
</script>
```

3. form 요소에 이벤트 핸들러 할당, submit 이벤트의 기본 동작 취소

```javascript
// accounts/profile.html

formTag.addEventListener("submit", function (event) {
  event.preventDefault();
});
```

4. axios 요청 작성

```javascript
formTag.addEventListener('submit', function (event) {
  event.preventDefault()
  axios({
    method: 'post',
    url: `/accounts/${}/follow/`,
  })
})
```

5. url에 작성할 user pk 가져오기 (html => javascript)

```html
<!-- accounts/profile.html -->
<form id="follow-form" data-user-id="{{ person.pk }}">...</form>

<script>
  formTag.addEventListener('submit', function (event) {
    event.preventDefault()

    const userId = event.currentTarget.dataset.userId
    const userId = this.dataset.userId
    const userId = formTag.dataset.userId
    axios({
      method: 'post',
      url: `/accounts/${}/follow/`,
    })
  })
</script>
```

- data-\* 속성
  - 사용자 지정 데이터 특성을 만들어 임의의 데이터를 HTML과 DOM 사이에서 교환할 수 있는 방법
  - 모든 사용자 지정 데이터는 JS에서 dataset 속성을 통해 사용
  - 주의사항
  1. 대소문자 여부에 상관없이 'xml' 문자로 시작 불가
  2. 세미콜론 포함 불가
  3. 대문자 포함 불가

```html
<!-- data-* 예시 -->
<div data-my-id="my-data"></div>

<script>
  const myId = event.target.dataset.myId;
</script>
```

6. 요청 url 작성 마무리

```javascript
formTag.addEventListener("submit", function (event) {
  event.preventDefault();

  const userId = event.currentTarget.dataset.userId;

  axios({
    method: "post",
    url: `/accounts/${userId}/follow/`,
  });
});
```

7. csrf token 데이터를 axios로 전송해야 함

```html
<!-- accounts/profile.html -->
<form id="follow-form" data-user-id="{{ person.pk }}">
  {% csrf_token %} {% if request.user in person.followers.all %}
  <input type="submit" value="언팔로우" />
  {% else %}
  <input type="submit" value="팔로우" />
  {% endif %}
</form>
```

8. csrf값을 가진 input 요소를 직접 선택 후 axios에 작성

```javascript
const csrftoken = document.querySelector("[name=csrfmiddlewaretoken]").value;

formTag.addEventListener("submit", function (event) {
  event.preventDefault();

  const userId = event.currentTarget.dataset.userId;

  axios({
    method: "post",
    url: `/accounts/${userId}/follow/`,
    headers: { "X-CSRFToken": csrftoken },
  });
});
```

9. 팔로우 버튼을 토글하기 위해서는 현재 팔로우 상태인지 상태 확인 필요

-> view 함수에서 팔로우 여부를 파악할 수 있는 변수를 추가로 생성해 JSON 타입으로 응답하기

10. 팔로우 상태 여부를 JS에게 전달할 데이터 작성
    응답은 더 이상 HTML 문서가 아닌 JSON 데이터로 응답

```python
# accounts/views.py

from django.http import JsonResponse

@login_required
def follow(request, user_pk):
    me = request.user
    you = get_user_model().objects.get(pk=user_pk)

    if me != you:
      if you.followers.filter(pk=me.pk).exists():
          you.followers.remove(me)
          is_followed = False
      else:
          you.followers.add(me)
          is_followed = True
      context = {
        'is_followed': is_followed
      }
      return JsonResponse(context)
    return redirect('accounts:profile', you.username)
```

11. 응답 데이터 is_followed에 따라 팔로우 버튼 토글

```javascript
axios({
  method: "post",
  url: `/accounts/${userId}/follow/`,
  headers: { "X-CSRFToken": csrftoken },
}).then((response) => {
  const isFollowed = response.data.is_followed;
  const followBtn = document.querySelector("input[type=submit]");
  if (isFollowed === true) {
    followBtn.value = "Unfollow";
  } else {
    followBtn.value = "Follow";
  }
});
```

12. 팔로잉 수와 팔로워 수 비동기 적용, 해당 요소 선택 위해 span 태그 작성

```html
<div>
  팔로잉 :
  <span id="followings-count">{{ person.followings.all|length }}</span> / 팔로워
  : <span id="followers-count">{{ person.followers.all|length }}</span>
</div>
```

13. view 함수에서 팔로워, 팔로잉 인원 수 연산을 진행하여 결과를 응답 데이터로 전달

```python
def follow(request, user_pk):
  ...
  context = {
    'is_followed': is_followed,
    'followings_count' : you.followings.count(),
    'followers_count' : you.followers.count(),
  }
  return JsonResponse(context)
```

14. 응답 데이터 받아 각 태그에 인원수 값 변경

```javascript
...
  .then((response) => {
    ...
    const followingsCountTag = document.querySelector('#followings-count')
    const followersCountTag = document.querySelector('#followers-count')

    followingsCountTag.textContent = response.data.followings_count
    followersCountTag.textContent = response.data.followers_count
  })
```

## Ajax with likes

### 비동기 좋아요 구현

좋아요 버튼은 한 페이지에 여러 개 존재

-> 버블링 활용하기!!!

1. 모든 좋아요 form 요소를 포함하는 최상위 요소 작성

```html
<!-- articles/index.html -->

<article class="article-container">
  {% for article in articles %} ... {% endfor %}
</article>
```

2. 최상위 요소 선택후 이벤트 핸들러 할당

```javascript
const articleContainer = document.querySelector(".article-container");

articleContainer.addEventListener("submit", function (event) {
  event.preventDefault();
});
```

3. axios 작성

```javascript
const articleContainer = document.querySelector('.article-container')

articleContainer.addEventListener('submit', function (event) {
  event.preventDefault()
  axios({
    method: 'post',
    url: `/articles/${}/likes`,
    headers: { "X-CSRFToken": csrftoken },
  })
})
```

4. 각 좋아요 form에 article.pk 부여 후 HTML의 article.pk 값을 JS에서 참조

```html
<form data-article-id="{{ article.pk }}">...</form>

<script>
  articleContainer.addEventListener("submit", function (event) {
    event.preventDefault();
    const articleId = event.target.dataset.articleId;
  });
</script>
```

5. url 완성 후 요청 및 응답 확인

```javascript
articleContainer.addEventListener("submit", function (event) {
  event.preventDefault();
  const articleId = event.target.dataset.articleId;

  axios({
    method: "post",
    url: `/articles/${articleId}/likes`,
    headers: { "X-CSRFToken": csrftoken },
  })
    .then((response) => {})
    .catch((error) => {
      console.log(error);
    });
});
```

6. 좋아요 상태 여부를 JS에게 전달할 데이터 작성 및 JSON 데이터 응답

```python
from django.http import JsonResponse

@login_required
def likes(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.user in article.like_users.all():
        article.like_users.remove(request.user)
        is_liked = False
    else:
        article.like_users.add(request.user)
        is_liked = True
    context = {
        'is_liked': is_liked
    }
    return JsonResponse(context)

```

7. 응답 데이터 받아서 적용

```javascript
axios({
  method: "post",
  url: `/articles/${articleId}/likes`,
  headers: { "X-CSRFToken": csrftoken },
})
  .then((response) => {
    const isLiked = response.data.is_liked;
  })
  .catch((error) => {
    console.log(error);
  });
```

8. 좋아요 버튼 토글 -> 버튼의 id 속성 값 설정

```html
{% if request.user in article.like_users.all %}
<input type="submit" value="좋아요 취소" id="like-{{ article.pk }}" />
{% else %}
<input type="submit" value="좋아요" id="like-{{ article.pk }}" />
{% endif %}
```

9. 좋아요 버튼 토글

```javascript
.then((response) => {
  const isLiked = response.data.is_liked;
  const likeBtn = document.querySelector(`#like-${articleId}`)
  if (isLiked === true){
    likeBtn.value = '좋아요 취소'
  } else {
    likeBtn.value = '좋아요'
  }
})
```
