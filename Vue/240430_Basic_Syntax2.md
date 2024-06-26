## Computed Properties

### Compouted

계산된 속성을 정의하는 함수

-> 미리 계산된 속성을 사용하여 템플릿에서 표현식을 단순하게 하고 불필요한 반복 연산을 줄임

- 할 일이 남았는지 여부에 따라 다른 메시지 출력

  ```html
  <h2>남은 할 일</h2>
  <p>{{ todos.length > 0 ? '아직 남았다' : '퇴근!' }}</p>
  ```

  ```js
  const todos = ref([
    { text: "Vue 실습" },
    { text: "자격증 공부" },
    { text: "TIL 작성" },
  ]);
  ```

  => computed 적용하면

  ```js
  const { createApp, ref, computed } = Vue;

  const restOfTodos = computed(() => {
    return todos.value.length > 0 ? "아직 남았다" : "퇴근!";
  });
  ```

  ```html
  <h2>남은 할 일</h2>
  <p>{{ restOfTodos }}</p>
  ```

#### 특징

반환되는 값은 computed ref이며 일반 refs와 유사하게 계산된 결과를 .value로 참조할 수 있음

computed 속성은 의존된 반응형 데이터를 자동으로 추적

의존하는 데이터가 변경될 때만 재평가

- restOfTodos는 todos가 변경될 때만 업데이트 됨

### Computed vs Methods

computed 속성 대신 method로도 동일한 기능을 정의할 수 있음

```js
const getRestOfTodos = function () {
  return todos.value.length > 0 ? "아직 남았다" : "퇴근!";
};
```

```html
<p>{{ getRestOfTodos() }}</p>
```

두개의 차이는

- computed 속성은 의존된 반응형 데이터를 기반으로 캐시된다.

  - 의존하는 데이터가 변경되지 않는 한 이미 계산된 결과에 대한 여러 참조는 다시 평가할 필요 없이 이전에 계산된 결과를 즉시 반환

- method 호출은 다시 렌더링이 발생할 때마다 항상 함수를 실행

#### Cache (캐시)

데이터나 결과를 일시적으로 저장해두는 임시 저장소

이후에 같은 데이터나 결과를 다시 계산하지 않고 빠르게 접근할 수 있도록 함

예를 들어, 웹 페이지의 캐시 데이터는 과거 방문한 적이 있는 페이지에 다시 접속할 경우 사용되는데,

페이지 일부 데이터를 브라우저 캐시에 저장 후 같은 페이지에 다시 요청 시 모든 데이터를 다시 응답 받는 것이 아닌 일부 캐시 된 데이터를 사용하여 더 빠르게 웹페이지를 렌더링한다.

#### computed와 method 사용처

- computed
  - 의존하는 데이터에 따라 결과가 바뀌는 계산된 속성을 만들 때 유용
  - 동일한 의존성을 가진 여러 곳에서 사용할 때 계산 결과를 캐싱하여 중복 계산 방지
- method
  - 단순히 특정 동작을 수행하는 함수를 정의할 때 사용
  - 데이터에 의존하는지 여부와 관계없이 항상 동일한 결과를 반환하는 함수

#### 정리하자면,

computed는 의존된 데이터가 변경되면 자동으로 업데이트 되고,

method는 호출해야만 실행됨

-> 무조건 computed만 사용하는 것이 아니라 사용 목적과 상황에 맞게 computed와 method를 적절히 조합하여 사용해야한다!

## Conditional Rendering

### v-if

표현식 값의 true/false를 기반으로 요소를 조건부로 렌더링

v-else를 사용하여 v-if에 대한 else 블록을 나타낼 수 있음

```js
const isSeen = ref(true);
```

```html
<p v-if="isSeen">true일때 보여요</p>
<p v-else>false일때 보여요</p>
<button @click="isSeen = !isSeen">토글</button>
```

v-else-if를 사용하여 v-if에 대한 else if 블록을 나타낼 수 있음

```js
const name = ref("Cathy");
```

```html
<div v-if="name === 'Alice'">Alice입니다</div>
<div v-else-if="name === 'Bella'">Bella입니다</div>
<div v-else-if="name === 'Cathy'">Cathy입니다</div>
<div v-else>아무도 아닙니다.</div>
```

#### HTML `<template>` element

페이지가 로드 될 때 렌더링 되지 않지만, JS를 사용하여 나중에 문서에서 사용할 수 있도록 하는 HTML을 보유하기 위한 메커니즘

-> 보이지 않는 wrapper 역할

HTML template 요소에 v-if를 사용하여 하나 이상의 요소에 대해 적용할 수 있음

```html
<template v-if="name === 'Cathy'">
  <div>Cathy입니다</div>
  <div>나이는 30살입니다</div>
</template>
```

### v-show

표현식 값의 true/false를 기반으로 요소의 가시성을 전환

v-show 요소는 항상 DOM에 렌더링 되어있음

- CSS display 속성만 전환하기 때문

```js
const isShow = ref(false);
```

```html
<div v-show="isShow">v-show</div>
<!-- <div style="display: none;">v-show</div> -->
```

#### v-if와 v-show의 적절한 사용처

- v-if (Cheap initial load, expensive toggle)
  - 초기 조건이 false인 경우 아무 작업도 수행하지 않음
  - 토글 비용이 높음
- v-show (Expensive initial load, cheap toggle)
  - 초기 조건에 관계 없이 항상 렌더링
  - 초기 렌더링 비용이 높음

-> 콘텐츠를 자주 전환해야 하는 경우에는 v-show, 실행중에 조건이 변경되지 않는 경우에는 v-if를 권장

## List Rendering

### v-for

소스 데이터를 기반으로 요소 또는 템플릿 블록을 여러 번 렌더링

alias in expression 형식의 특수 구문을 사용

```html
<div v-for="item in items">{{ item.text }}</div>
```

인덱스에 대한 별칭을 지정할 수 있음

```html
<div v-for="(item, index) in arr"></div>

<div v-for="value in object"></div>
<div v-for="(value, key) in object"></div>
<div v-for="(value, key, index) in object"></div>
```

배열 반복

```js
const myArr = ref([
  { name: "Alice", age: 20 },
  { name: "Bella", age: 21 },
]);
```

```html
<div v-for="(item, index) in myArr">{{index}} / {{item}}</div>
<!-- 결과
0 / { "name": "Alice", "age": 20 }
1 / { "name": "Bella", "age": 21 } 
-->
```

객체 반복

```js
const myObj = ref({
  name: "Cathy",
  age: 30,
});
```

```html
<div v-for="(value, key, index) in myObj">{{index}} / {{key}} / {{value}}</div>
<!-- 결과
0 / name / Cathy
1 / age / 30
 -->
```

HTML template 요소에 v-for을 사용하여 하나 이상의 요소에 대해 반복 렌더링 할 수 있음

```html
<ul>
  <template v-for="item in myArr">
    <li>{{ item.name }}</li>
    <li>{{ item.age }}</li>
    <hr />
  </template>
</ul>
```

각 v-for 범위는 상위 범위에 접근할 수 있음 (중첩 v-for)

```js
const myInfo = ref([
  { name: "Alice", age: 20, friends: ["Bella", "Cathy", "Dan"] },
  { name: "Bella", age: 21, friends: ["Alice", "Cathy"] },
]);
```

```html
<ul v-for="item in myInfo">
  <li v-for="friend in item.friends">{{ item.name }} - {{ friend }}</li>
</ul>
```

### v-for with key

반드시 v-for과 key를 함께 사용하여 내부 컴포넌트의 상태를 일관되게 하여 데이터의 예측 가능한 행동을 유지하기 위함

key는 반드시 각 요소에 대한 고유한 값을 나타낼 수 있는 식별자여야 함

```js
let id = 0;

const items = ref([
  { id: id++, name: "Alice" },
  { id: id++, name: "Bella" },
]);
```

```html
<div v-for="item in items" :key="item.id">
  <!-- content -->
</div>
```

#### 내장 특수 속성 key

- number 혹은 string으로만 사용해야 함
- Vue의 내부 가상 DOM 알고리즘이 이전 목록과 새 노드 목록을 비교할 때 각 node를 식별하는 용도로 사용
- Vue 내부 동작 관련된 부분이기에 최대한 작성하려고 노력할 것!!

### v-for with v-if

동일 요소에 v-for과 v-if를 함께 사용하지 않도록 유의할 것

동일한 요소에서 v-if가 v-for보다 우선순위가 높기 때문

-> v-if에서의 조건은 v-for 범위의 변수에 접근할 수 없음

#### 문제 상황

todo 데이터 중 이미 처리한 (isComplete === true) todo만 출력하기

```js
let id = 0;

const todos = ref([
  { id: id++, name: "복습", isComplete: true },
  { id: id++, name: "예습", isComplete: false },
  { id: id++, name: "저녁식사", isComplete: true },
  { id: id++, name: "노래방", isComplete: false },
]);
```

```html
<ul>
  <li v-for="todo in todos" v-if="!todo.isComplete" :key="todo.id"></li>
</ul>

<!-- Uncaught TypeError: Cannot read properties of undefined (reading 'isComplete') -->
```

#### 해결법 1. computed 활용

computed를 활용해 필터링 된 목록을 반환하여 반복하도록 설정

```js
const completeTodos = computed(() => {
  return todos.value.filter((todo) => !todo.isComplete);
});
```

```html
<ul>
  <li v-for="todo in completeTodos" :key="todo.id">{{ todo.name }}</li>
</ul>
```

#### 해결법 2. v-for과 `<template>` 요소 활용

```html
<ul>
  <template v-for="todo in todos" :key="todo.id">
    <li v-if="!todo.isComplete">{{ todo.name }}</li>
  </template>
</ul>
```

## Watchers

### watch

하나 이상의 반응형 데이터를 감시하고, 감시하는 데이터가 변경되면 콜백 함수 호출

#### 구조

```js
watch(source, (newValue, oldValue) => {
  // do something
});
```

- 첫번째 인자 source
  - watch가 감시하는 대상 (반응형 변수, 값을 반환하는 함수)
- 두번째 인자 callback function
  - source가 변경될 때 호출된느 콜백 함수
  - newValue : 감시하는 대상이 변화된 값
  - oldValue : 감시하는 대상의 기존 값

```html
<!-- 1 -->
<button @click="count++">Add 1</button>
<p>Count: {{ count }}</p>

<!-- 2 -->
<input v-model="message" />
<p>Message length: {{ messageLength }}</p>
```

```js
const count = ref(0);

watch(count, (newValue, oldValue) => {
  console.log(`newValue: ${newValue}, oldValue: ${oldValue}`);
});

const message = ref("");
const messageLength = ref(0);

watch(message, (newValue) => {
  messageLength.value = newValue.length;
});
```

여러 source를 감시하기 위해서는 배열을 활용함

```js
watch([foo, bar], ([newFoo, newBar], [prevFoo, prevBar]) => {
  // do something
});
```

### computed vs watch

![computed_watchers](./asset/computed_watcher.png)

## LifeCycle Hooks

Vue 인스턴스 생애주기 동안 특정 시점에 실행되는 함수

#### 예시

1. vue 컴포넌트 인스턴스가 초기 렌더링 및 DOM 요소 생성이 완료된 후 특정 로직을 수행

```js
const { crateApp, ref, onMounted } = Vue;

const app = createApp({
  setup() {
    onMounted(() => {
      console.log("mounted");
    });
  },
});
```

2. 반응형 데이터의 변경으로 인해 컴포넌트의 DOM이 업데이트된 후 특정 로직 수행

```html
<button @click="count++">Add 1</button>
<p>Count: {{ count }}</p>
<p>{{ message }}</p>
```

```js
const { createApp, ref, onMounted, onUpdated } = Vue;

const app = createApp({
  setup() {
    const count = ref(0);
    const message = ref(null);

    onUpdated(() => {
      message.value = "updated!";
    });
  },
});
```

#### 특징

Vue는 Lifecycle Hooks에 등록된 콜백 함수들을 인스턴스와 자동으로 연결

이렇게 동작하려면 hooks의 함수들은 반드시 동기적으로 작성되어야 함

인스턴스 생애 주기의 여러 단계에서 호출되는 다른 hooks도 있으며, 가장 일반적으로 사용되는 것은 onMounted, onUpdated, onUnmounted

## Vue Style Guide

우선순위에 따라 4가지 범주로 나눔

A. 필수

- 오류를 방지하는데 도움이 되므로 어떤 경우에도 규칙을 학습하고 준수
  ex) v-for에 key 작성, 동일 요소에 v-if와 v-for 함께 사용하지 않기

B. 적극 권장

- 가독성 및 개발자 경험을 향상시킴
- 규칙을 어겨도 코드는 여전히 실행되겠지만, 적당한 사유가 있어야 규칙을 위반할 수 있음

C. 권장

- 일관성을 보장하도록 임의의 선택을 할 수 있음

D. 주의 필요

- 잠재적 위험 특성을 고려

## 참고

### computed 주의사항

❗반환값은 변경하지 말 것❗

computed의 반환 값은 의존하는 데이터의 파생된 값
-> 이미 의존하는 데이터에 의해 계산이 완료 된 값

일종의 snapshot이며 의존하는 데이터가 변경될 때만 새 snapshot이 생성됨

계산된 값은 읽기 전용으로 취급되어야 하며, 변경되어서는 안됨

대신 새 값을 얻기 위해서는 의존하는 데이터를 업데이트 해야 함

만약 reverse나 sort 사용 시 원본 배열을 변경하기 때문에 원본 배열의 복사본을 만들어서 진행해야 함

-> `return [...numbers].reverse()`

### 배열 변경 관련 메서드

1. 변경 메서드
   1. 호출하는 원본 배열을 변경
   2. push(), pop, shift, unshift, splice, sort, reverse
2. 배열 교체
   1. 원본배열을 수정하지 않고 항상 새 배열을 반환
   2. filter(), concat, slice

### v-for과 배열을 활용해 필터링/정렬 활용하기

원본 데이터를 수정하거나 교체하지 않고 필터링하거나 정렬된 새로운 데이터를 표시하는 방법

1. computed 활용

원본 기반으로 필터링 된 새로운 결과를 생성

```js
const numbers = ref([1, 2, 3, 4, 5]);

const evenNumbers = computhed(() => {
  return numbers.value.filter((number) => number % 2 === 0);
});
```

```html
<ul>
  <li v-for="num in evenNumbers">{{num}}</li>
</ul
```

2. method 활용 (computed가 불가능한 중첩된 v-for에 경우 사용)

```js
const numberSets = ref([
  [1, 2, 3, 4, 5],
  [6, 7, 8, 9, 10],
]);

const evenNumberSets = function (numbers) {
  return numbers.filter((number) => number % 2 === 0);
};
```

```html
<ul v-for="numbers in numberSets">
  <li v-for="num in evenNumberSets(numbers)">{{num}}</li>
</ul>
```

### 배열의 인덱스를 v-for의 key로 사용하지 말 것

인덱스는 식별자가 아닌 배열의 항목 위치만 나타내기 때문

만약 새 요소가 배열의 끝이 아닌 위치 삽입되면 이미 반복된 구성 요소 데이터가 함께 업데이트되지 않기 때문

-> 직접 고유한 값을 만들어내는 메서드를 만들거나 외부 라이브러리등을 활용하는 등 식별자 역할을 할 수 있는 값을 만들어 사용

```html
<!-- 금지 -->
<div v-for="(item, index) in items" :key="index">
  <!-- content -->
</div>
```
