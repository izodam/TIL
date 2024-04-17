
## 변수
### 변수 선언 키워드
- 변수명 작성 규칙
	- 반드시 문자, 달러($), 밑줄( _ )로 시작
	- 대소문자를 구분
	- 예약어 사용 불가

- 변수명 Naming case
	- 카멜 케이스(camelCase) : 변수, 객체, 함수에 사용
	- 파스칼 케이스(PascalCase) :  클래스, 생성자에 사용
	- 대문자 스네이트 케이스(SNAKE_CASE) : 상수에 사용

- 선언 키워드
1. let
	블록 스코프를 갖는 지역 변수를 선언
	재할당 가능
	재선언 불가능
2.  const
	블록 스코프를 갖는 지역 변수를 선언
	재할당 불가능
	재선언 불가능
	선언시 반드시 초기값 설정 필요
3. var

```javascript
let number = 10  // 1. 선언 및 초기값 할등
number = 20     // 2. 재할당

let number = 10   // 1. 선언 및 초기값 할당
let number = 20   // 2. 재선언 불가능

// --------------------------
const number = 10    // 1. 선언 및 초기값 할당
number = 10        // 2. 재할당 불가능. Uncaught SyntaxError: Identifier 'secondNumber' has already been declared

const number = 10   // 1. 선언 및 초기값 할당
const number = 20   // 2. 재선언 불가능. Uncaught TypeError: Assignment to constant variable.

const number     // const declartions must be initailzed
```

- 블록 스코프
	- if, for 함수 등의 **중괄호 내부**를 가리킴
	- 블록 스코프를 가지는 변수는 블록 바깥에서 접근 불가능

기본적으로 const 사용을 권장하고, 재할당이 필요하다면 그때 let으로 변경해서 사용한다!!!!


## 데이터 타입
### 원시 자료형
Number, String, Boolean, null, undefined
변수에 값이 직접 저장되는 자료형 (불변, 값이 복사)
변수에 할당될 때 값이 복사됨
-> 변수 간에 서로 영향을 미치지 않음
```javascript
const bar = 'bar'
console.log(bar) // bar

bar.toUpperCase()
console.log(bar) // bar
```

```javascript
let a = 10
let b = a
b = 20
console.log(a)    // 10
console.log(b)    // 20
```

1. Number
정수 또는 실수형 숫자를 표현하는 자료형
```javascript
const a = 13
const b = -5
const c = 3.14
const d = 2.009e8
const e = Infinity
const f = -Infinity
const g = NaN   // Not a Number
```

2. String
텍스트 데이터를 표현하는 자료형
' + ' 연산자를 사용해 문자열끼리 결합
뺄셈, 곱셈, 나눗셈 불가능
```javascript
const firstName = 'Tony'
const lastName = 'Stark'
const fullName = firstName + lastName

console.log(fullname)  // TonyStark
```
- 템플릿 리터럴
내장된 표현식을 허용하는 문자열  작성 방식
backtick을 이용하며, 여러 줄에 걸쳐 문자열을 정의할 수도 있고 javascript의 변수를 문자열 안에 연결할 수 있음
```javascript
const age = 100
const message = `홍길동은 ${age}세 입니다.`
```

3. null
변수의 값이 없음을 의도적으로 표현할 때 사용
```javascript
let a = null
console.log(a)   // null
```

4. undefined
```javascript
let b
console.log(b)   // undefined
```

- 값이 없음을 나타내는 것이 null, undefined 2가지인 이유
설계 실수...
null이 원시 자료형임에도 typeof를 출력하면 object로 출력되는데, 그 이유는 javascript 설계 당시의 버그를 해결하지 않은 것.
-> 해결 못한 이유는 이미 null 타입에 의존성을 띄고 있는 수 많은 프로그램들이 망가질 수 있기 때문(하위 호환 유지)

5. Boolean
조건문 또는 반복문에서 boolean이 아닌 데이터 타입은 자동 형변환 규칙에 따라 true / false로 변환됨
- 자동 형변환

|  데이터 타입   |   false    |   true    |
| :-------: | :--------: | :-------: |
| undefined |  항상 false  |     .     |
|   null    |  항상 false  |     .     |
|  Number   | 0, -0, NaN | 나머지 모든 경우 |
|  String   | '' (빈 문자열) | 나머지 모든 경우 |


### 참조 자료형
Objects (Object, Array, Function)
객체의 주소가 저장되는 자료형 (가변, 주소가 복사)
객체를 생성하면 객체의 메모리 주소를 변수에 할당
-> 변수 간에 서로 영향을 미침
```javascript
const obj1 = { name: 'Alice', age: 30 }
const obj2 = obj1
obj2.age = 40

console.log(obj.age)      // 40
console.log(obj.age)      // 40
```


## 연산자
### 할당 연산자
오른쪽에 있는 피연산자의 평가 결과를 왼쪽 피연산자에 할당하는 연산자
단축 연산자 지원
```javascript
let a = 0

a += 10
a -= 3
a *= 10
a %= 7
```

### 증가 & 감소 연산자
- 증가 연산자 ("++")
피연산자를 증가(1을 더함)시키고 연산자의 위치에 따라 증가하기 전이나 후의 값을 반환
- 감소 연산자 ("--")
피연산자를 감소(1을 뺌)시키고 연산자의 위치에 따라 감소하기 전이나 후의 값을 반환
```javascript
let x = 3
const y = x++
console.log(x, y)  // 4 3

let a = 3
const b = ++a
console.log(a, b)  // 4 4
```

- 전위 연산자 : 연산자를 앞에 쓰는 경우. 피연산자에 1을 더한 값을 반환
- 후위 연산자 : 연산자를 뒤에 쓰는 경우. 피연산자에 1을 더하기 전의 값을 반환

### 비교 연산자
피연산자들(숫자, 문자, Boolean 등)을 비교하고 결과 값을 boolean으로 반환하는 연산자
```javascript
3 > 2    // true
3 < 2    // false

'A' < 'B'  // true
'Z' < 'a'  // true
'가' < '나'  // true
```

### 동등 연산자 ( == )
두 피연산자가 같은 값으로 평가되는지 비교 후 boolean 값을 반환
암묵적 타입 변환 통해 탕비을 일치시킨 후 같은 값인지 비교
두 피연산자가 모두 객체일 경우 메모리의 같은 객체를 바라보는지 판별
```javascript
console.log(1 == 1)   // true
console.log('hello' == 'hello')   // true
console.log('1' == 1)   // true
console.log(0 == false)   // true
```

### 일치 연산자 ( === )
두 피연산자의 **값과 타입이 모두 같은 경우** true를 반환
같은 객체를 가리키거나, 같은 타입이면서 같은 값인지를 비교
엄격한 비교가 이뤄지며 암묵적 타입 변환이 발생하지 않음
특수한 경우를 제외하고는 동등 연산자가 아닌 일치 연산자 사용 권장
```javascript
console.log(1 === 1)   // true
console.log('hello' === 'hello')   // true
console.log('1' === 1)   // false
console.log(0 === false)   // false
```

### 논리 연산자
and 연산 = &&
or 연산 = ||
not 연산 = !
단축 평가 지원

```javascript
true && false    // false
true && true    // true

false || true    // true
false || false    // false

!true    // false

1 && 0     // 0
0 && 1     // 0
4 && 7     // 7
1 || 0     // 1
0 || 1     // 1
4 || 7     // 4
```

## 조건문
### if
조건 표현식의 결과값을 boolean 타입으로 변환 후 참/거짓을 판단
```javascript
const name = 'customer'

if (name === 'admin') {
	console.log('관리자님 환영해요')
} else if (name === 'customer'){
	console.log('고객님 환영해요')
} else {
	console.log(`반갑습니다. ${name}님`)
}
```

### 삼항 연산자
`condition ? expression1 : expression2`
condition : 평가할 조건
expression1 : 조건이 true일때 반환할 값
expression2 : 조건이 false일때 반환할 값
```javascript
const age = 20
const message = (age >= 18) ? '성인' : '미성년자'

console.log(message)   // 성인
```

## 반복문
### while
조건문이 참이면 문장을 계속해서 수행
```javascript
while (조건문) {
	// do something
}
```
### for
특정한 조건이 거짓으로 판별될 때까지 반복
```javascript
for ([초기문]; [조건문]; [증감문]) {
	// do something
}
```

ex)
```javascript
for (let i = 0; i < 6; i++){
	console.log(i)
}
```
### for ... in
객체의 열거 가능한 속성에 대해 반복
```javascript
for (variable in object){
	statement
}
```

ex)
```javascript
const fruits = {
  a: 'apple',
  b: 'banana'
}

for(const property in fruits) {
	console.log(property) // a, b
	console.log(fruits[property]) // apple, banana
}
```
### for ... of
반복 가능한 객체(배열, 문자열 등)에 대해 반복
```javascript
for (variable of iterable) {
	statement
}
```

ex)
```javascript
const numbers = [0, 1, 2, 3]

for (const number of numbers) {
	console.log(number)
}
```

### 배열 반복과 for .. in
객체 관점에서 배열의 인덱스는 정수 이름을 가진 열거 가능한 속성
for .. in 은 정수가 아닌 이름과 속성을 포함하여 열거 가능한 모든 속성을 반환
내부적으로 for .. in 은 배열의 반복자가 아닌 속성 열거를 사용하기 때문에 특정 순서에 따라 인덱스를 반환하는 것을 보장할 수 없음

-> for .. in 은 인덱스 순서가 중요한 배열에서는 사용하지 않음..!!
배열은 for, for ..of 를 사용
-> 객체 관점에서 배열의 인덱스는 정수 이름을 가진 속성이기 때문에 인덱스가 출력 됨. (순서 보장 X)
```javascript
const arr = ['a', 'b', 'c']

for (const i in arr) {
	console.log(i)  // 0 1 2
}

for (const i of arr) {
	console.log(i) // a b c
}
```

### 반복문에서 const
for문에서는 최초 정의한 i에 대해서 재할당하면서 사용하기 때문에 const를 사용하면 에러 발생

for in, for of 에서는 재할당이 아니라 매 반복마다 다른 속성 이름이 변수에 지정되는 것이므로 const를 사용해도 에러가 발생하지 않음
단, const 특징에 따라 블록 내부에서 변수를 수정할 수 없음


## 참고
### 세미콜론
문장 마지막 세미콜론을 선택적으로 사용 가능
세미콜론이 없으면 ASI에 의해 자동으로 세미콜론이 삽입됨

### var
ES6 이전에 변수 선언에 사용했던 키워드
재할당 & 재선언 가능
함수 스코프를 가짐
호이스팅 되는 특성으로 인해 예기치 못한 문제 발생 가능

- 함수 스코프
	- 함수의 중괄호 내부를 가리킴

- 호이스팅
	- 변수를 선언 이전에 참조할 수 있는 현상
	- 변수 선언 이전의 위치에서 접근 시 undefined를 반환

### NaN 반환 예시
1. 숫자로서 읽을 수 없음
2. 결과가 허수인 수학 계산식 (Math.sqrt(-1))
3. 피연산자가 NaN (7 * NaN)
4. 정의할 수 없는 계산식 (0 * Infinity)
5. 문자열을 포함하면서 덧셈이 아닌 계산식 ('가' / 3)