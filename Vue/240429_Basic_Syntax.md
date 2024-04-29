## Template Syntax

DOM을 기본 구성 요소 인스턴스의 데이터에 선언적으로 바인딩할 수 있는 HTML 기반 템플릿 구문을 사용

### 종류

#### 1. Text Interpolation

데이터 바인딩의 가장 기본적인 형태

이중 중괄호 구문(콧수염 구문) 사용

콧수염 구문은 해당 구성 요소 인스턴스의 msg 속성 값으로 대체

msg 속성이 변경될 때마다 업데이트 됨

```javascript
<p>Message: {{ msg }}</p>
```

#### 2. Raw HTML

콧수염 구문은 데이터를 일반 텍스트로 해석하기 때문에 실제 HTML을 출력하려면 v-html을 사용해야 함

```html
<div v-html="rawHtml"></div>
<script>
  const rawHtml = ref('<span style="color:red">This sould be red.</span>');
</script>
```

#### 3. Attribute Bindings

콧수염 구문은 HTML 속성 내에 사용할 수 없기 때문에 v-bind를 사용

HTML의 id 속성 값을 vue의 dynamicId 속성과 동기화 되도록 함

바인딩 값이 null이나 undefind인 경우 렌더링 요소에서 제거됨

```html
<div v-bind:id="dynamicId"></div>
<script>
  const dynamicId = ref("my-id");
</script>
```

#### 4. JavaScript Expressions

Vue는 모든 데이터 바인딩 내에서 Javascript 표현식의 모든 기능을 지원

Vue 템플릿에서 Javascript 표현식을 사용할 수 있는 위치는

1. 콧수염 구문 내부
2. 모든 directive 속성 값 (v-로 시작하는 특수 속성)

```html
{{ number + 1 }} {{ ok ? 'YES' : 'NO' }} {{ message.split('').reverse().join('')
}}
<div :id="`list-${id}`"></div>
```

- 주의사항
  - 각 바인딩에는 하나의 단일 표현식만 포함될 수 있음
  - 표현식은 값으로 평가할 수 있는 코드조각(return 뒤에 사용할 수 있는 코드여야 함)

```html
<!-- 표현식이 아닌 선언식 -->
{{ const number = 1 }}

<!-- 제어문은 삼항 표현식을 사용해야 함 -->
{{ if (ok) { return message }}}
```

### Directive

'v-' 접두사가 있는 특수 속성

- 특징
  - Directive의 속성값은 단일 Javascript 표현식이어야 함
  - 표현식 값이 변경될 때 DOM에 반응적으로 업데이트를 적용

#### 구문

![](https://vuejs.org/assets/directive.DtZKvoAo.png)

- Arguments

  - 일부는 directive 뒤에 콜론(:)으로 표시되는 인자를 사용할 수 있음

  ```html
  <!-- a요소의 href 속성 값을 myUrl 값에 바인딩하도록 하는 v-bind의 인자 -->
  <a v-bind:href="myUrl">Link</a>

  <!-- click은 이벤트 수신할 이벤트 이름을 작성하는 v-on 인자 -->
  <button v-on:click="doSomething">Button</button>
  ```

- Modifiers
  - .(dot)으로 표시되는 특수 접미사
  - 특별한 방식으로 바인딩되어야 함을 나타냄
  ```html
  <!-- 발생한 이벤트에서 event.preventDefault()를 호출하도록 v-on에 지시하는 modifier -->
  <form @submit.prevent="onSubmit">...</form>
  ```

## Dynamically data binding

### v-bind

하나 이상의 속성 또는 컴포넌트 데이터를 표현식에 동적으로 바인딩

사용처

#### 1. Attribute Bindings

HTML 속성 값을 Vue의 상태 속성 값과 동기화 되도록 함

```html
<img v-bind:src="imageSrc" /> <a v-bind:href="myUrl">Move to url</a>
```

약어로 :만 사용하기도 함

```html
<img :src="imageSrc" /> <a :href="myUrl">Move to url</a>
```

Dynamic attribute name (동적 인자 이름)

- 대괄호[] 로 감싸서 directive argument에 JS 표현식을 사용할 수도 있음
- JS 표현식에 따라 동적으로 평가된 값이 최종 argument 값으로 사용됨
- 대문자 안에 작성하는 이름은 반드시 소문자로만 구성 가능 (브라우저가 속성 이름은 소문자로 강제 변환하기 때문)

```html
<button :[key]="myValue"></button>
```

```html
<div id="app">
  <img v-bind:src="imageSrc" />
  <a v-bind:href="myUrl">Move to url</a>
  <p :[dynamicattr]="dynamicValue">...</p>
</div>

<script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
<script>
  const { createApp, ref } = Vue;

  const app = createApp({
    setup() {
      const imageSrc = ref("https://picsum.photos/200");
      const myUrl = ref("https://www.google.co.kr/");
      const dynamicattr = ref("title");
      const dynamicValue = ref("Hello Vue.js");
      return {
        imageSrc,
        myUrl,
        dynamicattr,
        dynamicValue,
      };
    },
  });

  app.mount("#app");
</script>
```

#### 2. Class and Style Bindings

class와 style은 모두 HTML 속성이므로 다른 속성과 마찬가지로 v-bind를 사용하여 동적으로 문자열 값을 할당할 수 있음

Vue는 class 및 style 속성 값을 v-bind로 사용할 때 **객체 또는 배열**을 활용하여 작성할 수 있도록 함

-> 단순히 문자열 연결을 사용하여 이러한 값을 생성하는 것은 번거롭고 오류가 발생하기가 쉽기 때문

가능한 경우

1. Binding HTML Classes

   1. Binding to Objects

      - 객체를 :class에 전달하여 클래스를 동적으로 전환할 수 있음
      - `<div :class="{active:isActive}">Text</div>`
      - 객체에 더 많은 필드를 포함하여 여러 클래스를 전환할 수 있음
      - `<div :class="{active:isActive, 'text-primary': hasInfo}">Text</div>`
      - 반드시 inline 방식으로 작성하지 않아도 됨

      ```html
      <div class="static" :class="classObj">Text</div>

      <script>
        const isActive = ref(false);
        const hasInfo = ref(true);
        // ref는 반응 객체의 속성으로 액세스되거나 변경될 때 자동으로 unwrap
        const classObj = ref({
          active: isActive,
          "text-primary": hasInfo,
        });
      </script>
      ```

   2. Binding to Arrays
      - :class를 배열에 바인딩하여 클래스 목록을 적용할 수 있음
      - `<div :class="[activeClass, infoClass]">Text</div>`
      - 배열 구문 내에서 객체 구문을 사용하는 경우
      - `<div :class="[{active: isActive}, infoClass]">Text</div>`

2. Binding Inline Styles
   1. Binding to Objects
      - :style은 JS 객체 값에 대한 바인딩 지원
      - `<div :style="{color: activeColor, fontSize: fontSize + 'px'}">Text</div>`
      - 실제 CSS에서 사용하는 것처럼 :style은 kebab-cased 키 문자열도 지원
      - 반드시 inline 방식으로 작성하지 않아도 됨
   2. Binding to Arrays
      - 여러 스타일 객체를 배열에 작성해서 :style을 바인딩 할 수 있음
      - 작성한 객체는 병합되어 동일한 요소에 적용
      - `<div :style="[styleObj, styleObj2]">Text</div>`

## Event Handling

### v-on

DOM 요소에 이벤트 리스너를 연결 및 수신

- handler 종류
  - 1. inline handlers : 이벤트가 트리거 될 때 실행 될 코드
  - 2. Method handlers : 컴포넌트에 정의된 메서드 이름

약어로 @을 사용하기도 한다!!

#### 1. Inline handlers

주로 간단한 상황에 사용

```html
<button @click="count++">Add 1</button>
<p>Count: {{ count }}</p>

<script>
  const const = ref(0)
</script>
```

#### 2. Method Handlers

Inline으로는 불가능한 대부분의 상황에서 사용

```html
<button @click="myFunc">Hello</button>

<script>
  const name = ref("Alice");
  const myFunc = function (event) {
    console.log(event);
    console.log(event.currentTarget);
    console.log(`hello ${name.value}!`);
  };
</script>
```

트리거하는 기본 DOM Event 객체를 자동으로 수신

#### Inline Handlers에서의 메서드 호출

메서드 이름을 직접 바인딩하는 대신 Inline Handlers에서 메서드를 호출할 수도 있음

이렇게 하면 기본 이벤트 대신 사용자 지정 인자를 전달 할 수 있음

```html
<button @click="greeting('hello')">Say hello</button>

<script>
  const greeting = function (message) {
    console.log(message);
  };
</script>
```

#### Inline Handlers에서의 event 인자에 접근하기

$event 변수를 사용하여 메서드에 전달

`<button @click="warning('경고입니다.', $event)">Submit</button>`

#### Event Modifiers

stop, prevent, self 등 다양한 modifier을 제공

-> 메서드는 DOM 이벤트에 대한 처리보다는 데이터에 관한 논리를 작성하는 것에 집중할 것

#### Key modifiers

Vue는 키보드 이벤트 수신할 때 특정 키에 관한 별도 modifiers를 사용할 수 있음

`<input @keyup.enter="onSubmit">`

## Form Input Bindings

form을 처리할 때 사용자가 input에 입력하는 값을 실시간으로 JS 상태에 동기화해야 하는 경우 (양방향 바인딩)

1. v-bind와 v-on을 함께 사용

   1. v-bind를 사용하여 input 요소의 value 속성 값을 입력 값으로 사용
   2. v-ond을 사용하여 input 이벤트가 발생할 때마다 input 요소의 value값을 별도 반응형 변수에 저장하는 핸들러 호출

   ```html
   <p>{{ inputText1 }}</p>
   <input :value="inputText1" @input="onInput" />

   <script>
     const inputText1 = ref("");
     const onInput = function (event) {
       inputText1.value = event.currentTarget.value;
     };
   </script>
   ```

2. v-model 사용

### v-model

form input 요소 또는 컴포넌트에서 양방향 바인딩을 만듦

사용자 입력 데이터와 반응형 변수를 실시간 동기화

-> IME가 필요한 언어(한국어, 중국어, 일본어 ...)등의 경우 v-model이 제대로 업데이트 되지 않음

-> 해당 언어에 대해 올바르게 응답하려면 v-bind, v-on 방법을 사용해야 함

```html
<p>{{ inputText2 }}</p>
<input v-model="inputText2" />
```

#### 활용

v-model은 단순 Text input 뿐만 아니라 Checkbox, Radio, Select 등 다양한 타입의 사용자 입력 방식과 함께 사용 가능

#### 1. checkbox

1. 단일 체크박스
   체크 했을 때에는 label이 true, 체크를 풀으면 label이 false가 된다.

```html
<input type="checkbox" id="checkbox" v-model="checked" />
<label for="checkbox">{{ checked }}</label>
```

2. 여러 체크박스와 배열 활용

```html
<!-- multiple checkbox -->
<div>Checked names: {{ checkedNames }}</div>

<input type="checkbox" id="alice" value="Alice" v-model="checkedNames" />
<label for="alice">Alice</label>

<input type="checkbox" id="bella" value="Bella" v-model="checkedNames" />
<label for="bella">Bella</label>
```

#### 2. Select

select에서 v-model 표현식의 초기값이 어떤 option과도 일치하지 않는 경우 select 요소는 unselect 상태로 렌더링됨

```html
<select v-model="selected">
  <option disabled value="">Please select one</option>
  <option>Alice</option>
  <option>Bella</option>
  <option>Cathy</option>
</select>
```

## 참고

### $ 접두어가 붙은 변수

Vue 인스턴스 내에서 제공되는 내부 변수

사용자가 지정한 반응형 변수나 메서드를 구분하기 위함

주로 Vue 인스턴스 내부 상태를 다룰 때 사용

### IME(Input Method Editor)

사용자가 입력 장치에서 기본적으로 사용할 수 없는 문자(비영어권 언어)를 입력할 수 있도록 하는 운영 체제 구성 프로그램

일반적으로 키보드 키보다 자모가 더 많은 언어에서 사용해야 함

-> IME가 동작하는 방식과 Vue의 양방향 바인딩 (v-model) 동작 방식이 상충하기 때문에 한국어 입력 시 예상대로 동작하지 않았던 것
