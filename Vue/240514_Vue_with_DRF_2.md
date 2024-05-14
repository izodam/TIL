## Authentication with DRF

### 인증

수신된 요청을 해당 요청의 사용자 또는 자격 증명과 연결하는 메커니즘

-> 누구인지 확인하는 과정

#### permissions (권한)

요청에 대한 접근 허용 또는 거부 여부를 결정

#### 인증과 권한

순서상 인증이 먼저 진행되며 수신 요청을 해당 요청의 사용자 또는 해당 요청이 서명된 토큰(token)과 같은 자격 증명 자료와 연결

그런 다음 권한 및 제한 정책은 인증이 완료된 해당 자격 증명을 사용하여 요청을 허용해야 하는 지를 결정

DRF에서 인증은

항상 view 함수 시작 시, 권한 및 제한 확인이 발생하기 전, 다른 코드의 진행이 허용되기 전에 실행됨

인증 자체로는 들어오는 요청을 허용하거나 거부할 수 없으며, 단순히 요청에 사용된 자격증명만 식별!!

#### 승인되지 않은 응답 및 금지된 응답

1. HTTP 401 Unauthorized

요청된 리소스에 대한 유효한 인증 자격 증명이 없기 때문에 클라이언트 요청이 완료되지 않았음을 나타냄 (누구인지 증명할 자료가 없음)

2. HTTP 403 Forbidden (Permission Denien)

서버에 요청이 전달되었지만, 권한 때문에 거절되었다는 것을 의미

401과 다른점은 서버는 클라이언트가 누구인지는 알고 있음

### 인증 체계 설정

#### 1. 전역 설정

DEFAULT_AUTHENTICATION_CLASSES 사용

```py
REST_FRAMEWORK = {
    # Authentication
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
}
```

#### 2. view 함수 별 설정

authentication_classes 데코레이터 사용

```py
from rest_framework.decorators import permission_classes
from rest_framework.permissions import TokenAuthentication, BasicAuthentication

@api_view(['GET', 'POST'])
@permission_classes([TokenAuthentication, BasicAuthentication])
def article_list(request):
    pass
```

#### DRF가 제공하는 인증 체계

1. BasicAuthentication
2. TokenAuthentication
3. SessionAuthentication
4. RemoteUserAuthentication

#### TokenAuthentication

token 기반 HTTP 인증 체계

기본 데스크톱 및 모바일 클라이언트와 같은 클라이언트-서버 설정에 적합

-> 서버가 인증된 사용자에게 토큰을 발급하고 사용자는 매 요청마다 발급받은 토큰을 요청과 함께 보내 인증 과정 거침

### Token 인증 설정

과정

#### 1. 인증 클래스 설정

TokenAuthentication 활성화

```py
# settings.py

REST_FRAMEWORK = {
    # Authentication
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
}
```

#### 2. INSTALLED_APPS 추가

```py
# settings.py

INSTALLED_APPS = [
    'articles',
    'accounts',
    'rest_framework',
    'rest_framework.authtoken',
    ...,
]
```

#### 3. migrate 진행

#### 4. 토큰 생성 코드 작성

인증된 사용자에게 자동으로 토큰 생성

```py
# accounts/signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
```

### Dj-Rest-Auth 라이브러리

회원가입, 인증(소셜미디어 인증 등), 비밀번호 재설정, 사용자 세부 정보 검색, 회원 정보 수정 등 다양한 인증 관련 기능을 제공하는 라이브러리

1. 설치

```bash
$ pip install dj-rest-auth
```

2. app 등록

```py
INSTALLED_APPS = [
    'articles',
    'accounts',
    'rest_framework',
    'rest_framework.authtoken',
    'dj_rest_auth',
]
```

3. url 설정

```py
# my_api/urls.py

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('articles.urls')),
    path('accounts/', include('dj_rest_auth.urls')),
]

```

#### Registration(등록) 기능 추가 설정

1. 패키지 추가 설치

```bash
$ pip install 'dj-rest-auth[with_social]'
```

2. app 등록

```py
INSTALLED_APPS = [
    ...,
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'dj_rest_auth.registration',
]

SITE_ID = 1
```

3. 추가 설정

```py
# settings.py

ACCOUNT_EMAIL_VERIFICATION = 'none'

MIDDLEWARE = [
    ...,
    'allauth.account.middleware.AccountMiddleware',
]

```

4. 추가 url 등록

```py
# my_api/urls.py

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('articles.urls')),
    path('accounts/', include('dj_rest_auth.urls')),
    path('accounts/signup/', include('dj_rest_auth.registration.urls')),
]

```

5. migrate 진행

### Token 발급 및 활용

1. 회원가입 및 로그인을 진행하여 토큰 발급 테스트
2. `http://127.0.0.1:8000/accounts/signup/`에서 회원가입 진행
3. `http://127.0.0.1:8000/accounts/login/`에서 로그인 진행
4. 로그인 성공 후 DRF 로부터 발급받은 Token 확인

-> 이 토큰을 vue에서 별도로 저장하여 매 요청마다 함께 보내야 함

게시글 작성 요청시,

headers에 발급받은 Token 작성 후 요청 성공 확인

- key: "Authorization"
- Value: "Token 토큰값" (문자열 "Token"이 와야 하며 공백으로 두 문자열을 구분해야 함)

### 권한 정책 설정

#### 1. 전역 설정

DEFAULT_AUTHENTICATION_CLASSES 사용

```py
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}
```

지정하지 않을 경우 이 설정은 기본적으로 무제한 엑세스 허용

```py
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
}
```

#### 2. view 함수 별 설정

permission_classes 데코레이터 사용

```py
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def article_list(request):
  pass
```

#### DRF가 제공하는 권한 정책

1. IsAuthenticated
2. IsAdminUser
3. IsAuthenticatedOrReadOnly
4. ...

#### IsAuthenticated 권한

인증되지 않은 사용자에 대한 권한을 거부하고 그렇지 않은 경우 권한을 허용

=> 등록된 사용자만 API에 액세스 할 수 있도록 하려는 경우 적합

### IsAuthenticated 권한 설정

1. DEFAULT_AUTHENTICATION_CLASSES 설정

```py
# settings.py

REST_FRAMEWORK = {
    # Authentication
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    # permission
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
}
```

2. permission_classes 데코레이터 사용

```py
# articles/views.py

from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def article_list(request):
  pass
```

## Authentication with Vue

### 회원가입

1. route

```js
// router/index.js

{
  path: '/signup',
  name: 'SignUpView',
  component: SignUpView
},
```

2. RouterLink 작성

```vue
<!-- App.vue -->

<nav>
  <RouterLink :to="{ name: 'ArticleView' }">Articles</RouterLink> |
  <RouterLink :to="{ name: 'SignUpView' }">SignUpPage</RouterLink>
</nav>
```

3. 회원가입 form 작성

```vue
<!-- views/SignUpView.vue -->

<template>
  <div>
    <h1>Sign up Page</h1>
    <form>
      <label for="username">username : </label>
      <input type="text" id="username" v-model.trim="username" /><br />

      <label for="password1">password : </label>
      <input type="password" id="password1" v-model.trim="password1" /><br />

      <label for="password2">password confirmation : </label>
      <input type="password" id="password2" v-model.trim="password2" /><br />

      <input type="submit" value="SignUp" />
    </form>
  </div>
</template>
```

4. 사용자 입력 데이터 바인딩

```vue
<!-- views/SignUpView.vue -->

<script setup>
import { ref } from "vue";

const username = ref(null);
const password1 = ref(null);
const password2 = ref(null);
</script>
```

5. signUp 함수가 해야 할 일

-> 사용자 입력 데이터를 받아 서버로 회원가입 요청을 보냄

```js
// stores/counter.js

const signUp = function (payload) {
  const username = payload.username;
  const password1 = payload.password1;
  const password2 = payload.password2;

  axios({
    method: "post",
    url: `${API_URL}/accounts/signup/`,
    data: {
      username,
      password1,
      password2,
    },
  })
    .then((res) => {
      console.log("회원가입 완료");
    })
    .catch((err) => console.log(err));
};
return { articles, API_URL, getArticles, signUp };
```

6. 컴포넌트에 사용자 입력 데이터 저장 후 store의 signUp 호출

```js
// views/SignupView.vue

const store = useCounterStore();

const signUp = function () {
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value,
  };
  store.signUp(payload);
};
```

### 로그인

1. router 등록

```js
// router/index.js

{
  path: '/login',
  name: 'LogInView',
  component: LogInView
}
```

2. App 컴포넌트에 LogInView 컴포넌트로 이동하는 RouterLink 작성

```vue
<!-- App.vue -->

<nav>
  <RouterLink :to="{ name: 'ArticleView' }">Articles</RouterLink> |
  <RouterLink :to="{ name: 'SignUpView' }">SignUpPage</RouterLink> | 
  <RouterLink :to="{ name: 'LogInView' }">LoginPage</RouterLink>
</nav>
```

3. 로그인 form 작성

```vue
<!-- views/LoginView.vue -->

<template>
  <div>
    <h1>Login Page</h1>
    <form>
      <label for="username">username : </label>
      <input type="text" id="username" v-model.trim="username" /><br />

      <label for="password">password : </label>
      <input type="password" id="password" v-model.trim="password" /><br />

      <input type="submit" value="login" />
    </form>
  </div>
</template>
```

4. 사용자 입력 데이터 바인딩

```vue
<!-- views/LoginView.vue -->

<script setup>
import { ref } from "vue";

const username = ref(null);
const password = ref(null);
</script>
```

5. 로그인 요청을 보내기 위한 logIn 함수 작성

```js
// stores/counter.js

const logIn = function (payload) {
  const username = payload.username;
  const password = payload.password;
  axios({
    method: "post",
    url: `${API_URL}/accounts/login/`,
    data: {
      username,
      password,
    },
  })
    .then((res) => {
      console.log("로그인 완료");
      console.log(res.data);
    })
    .catch((err) => console.log(err));
};

return { articles, API_URL, getArticles, signUp, logIn };
```

6. 컴포넌트에 사용자 입력 데이터 저장 후 store의 logIn 함수 호출

```js
// views/LoginView.vue

const store = useCounterStore();

const logIn = function () {
  const payload = {
    username: username.value,
    password: password.value,
  };
  store.logIn(payload);
};
```

로그인 완료 시 응답 객체 안에 Django가 ㅂ잘급한 Token이 함께 옴

### 요청과 토큰

token을 store에 저장하여 인증이 필요한 요청마다 함께 보냄

```js
// stores/counter.js

const token = ref(null);

const logIn = function (payload) {
  ...
    .then((res) => {
      token.value = res.data.key
    })
    .catch((err) => console.log(err));
};

return { articles, API_URL, getArticles, signUp, logIn, token };
```

토큰이 필요한 요청

#### 1. 게시글 전체 목록 조회 시

```js
// stores/counter.js

const getArticles = function () {
      axios({
        method: "get",
        url: `${API_URL}/api/v1/articles/`,
        headers: {
          Authorization: `Token ${token.value}`
        }
      })
      ...
}
```

#### 2. 게시글 작성 시

```js
// views/CreateView.vue

const createArticle = function () {
  axios({
    method: 'post',
    url: `${store.API_URL}/api/v1/articles/`,
    data: {
      title: title.value,
      content: content.value
    },
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
  ...
}
```

### 인증 여부 확인

1. 인증되지 않은 사용자는 메인페이지 접근을 제한하고
2. 인증된 사용자는 회원가입 및 로그인 페이지에 접근을 제한하는 기능 구현

#### 인증상태 여부를 나타낼 속성값 지정

token 소유 여부에 따라 로그인 상태를 나타낼 isLogin 변수 작성

computed를 활용해 token값이 변할 때만 상태를 계산

```js
// stores/counter.js

const isLogin = computed(() => {
  if (token.value === null) {
    return false;
  } else {
    return true;
  }
});

return { articles, API_URL, getArticles, signUp, logIn, token, isLogin };
```

#### 1. 인증되지 않은 사용자는 메인페이지 접근을 제한

beforeEach를 활용해 다른 주소에서 메인 페이지로 이동 시 인증되지 않은 사용자라면 로그인 페이지로 이동시키기

```js
// router/index.js

import { useCounterStore } from "@/stores/counter";

const router = createRouter({...});

router.beforeEach((to, from) => {
  const store = useCounterStore();
  if (to.name === "ArticleView" && !store.isLogin) {
    window.alert("로그인이 필요합니다.");
    return { name: "LogInView" };
  }
});
```

#### 인증된 사용자는 회원가입 및 로그인 페이지에 접근을 제한

```js
// router/index.js

router.beforeEach((to, from) => {
  const store = useCounterStore();
  if (to.name === "ArticleView" && !store.isLogin) {
    window.alert("로그인이 필요합니다.");
    return { name: "LogInView" };
  }
  if ((to.name === "SignUpView" || to.name === "LogInView") && store.isLogin) {
    window.alert("이미 로그인 되어있습니다.");
    return { name: "ArticleView" };
  }
});
```

### 기타 기능 구현

#### 로그인 성공 후 자동으로 메인 페이지로 이동

```js
// stores/counter.js

const router = useRouter()

const logIn = function (payload) {
  ...
    .then((res) => {
      token.value = res.data.key;
      router.push({ name: "ArticleView" });
    })
};
```

#### 회원가입 성공 후 자동으로 로그인까지 진행

```js
// stores/counter.js

const signUp = function (payload) {
  ...
    .then((res) => {
      const password = password1;
      logIn({ username, password });
    })
};
```

## 참고

### Django Signals

이벤트 알림 시스템

애플리케이션 내에서 특정 이벤트가 발생할 때, 다른 부분에게 신호를 보내어 이벤트가 발생했음을 알릴 수 있음

주로 모델의 데이터 변경 또는 저장, 삭제와 같은 작업에 반응하여 추가적인 로직을 실행하고자 할 때 사용

### 환경변수 (environment variable)

애플리케이션의 설정이나 동작을 제어하기 위해 사용되는 변수

#### 목적

개발, 테스트 및 프로덕션 환경에서 다르게 설정되어야 하는 설정값이나 민감한 정보를 포함

환경변수를 사용하여 애플리케이션의 설정을 관리하면, 다양한 환경에서 일관된 동작을 유지하면서 필요에 따라 변수를 쉽게 변경할 수 있음

보안적인 이슈를 피하고, 애플리케이션을 다양한 환경에 대응하기 쉽게 만들어줌

#### Vite에서 환경변수 사용하는 법

https://ko.vitejs.dev/guide/env-and-mode
