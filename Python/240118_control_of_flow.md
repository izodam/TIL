# 제어문


- 코드의 실행 흐름을 제어하는 데 사용되는 구문
- **조건**에 따라 코드 블록을 실행하거나 **반복**적으로 코드를 실행

## 조건문

- 주어진 조건식을 평가하여 해당 조건이 **참(True)인 경우**에만 코드 블록을 실행하거나 건너뜀
- if / elif / else

### if

```python
if 표현식:
    코드 블록
elif 표현식:
    코드 블록
else:
    코드 블록
```

- 복수 조건문
    - 조건문을 동시에 검사하는 것이 아니라 순차적으로 비교



## 반복문

- 주어진 코드 블록을 여러 번 반복해서 실행하는 구문
- for / while

### for

- 임의의 시퀀스 항목들을 그 시퀀스에 들어있는 순서대로 반복

    ```python
    for 변수 in 반복 가능한 객체:
        코드 블록
    ```

- 반복 가능한 객체(iterable) : 반복문에서 순회할 수 있는 객체
    - 시퀀스 객체 뿐만 아니라 dict, set등도 포함
- 원리
    - 리스트 내 첫 항목이 반복 변수에 할당되고 코드 블록이 실행
    - 다음으로 반복 변수에 리스트의 두번째 항목이 할당되고 코드 블록이 실행
    - … 반복
- 문자열, range, 딕셔너리 순회도 가능!
    - 딕셔너리 순회는 key만 나옴
    
    ```python
    my_dict = {
        'x' : 10,
        'y' : 20,
        'z' : 30,
    }
    
    for key in my_dict:
        print(key)
    
    '''
    x
    y
    z
    '''
    ```
    
- 인덱스로 접근하여 리스트 순회도 가능함!

### while

- 주어진 조건식이 참(True)인 동안 코드를 반복해서 실행
- 조건식이 거짓(False)가 될 때까지 반복

    ```python
    while 조건식:
        코드 블록
    ```

- while 문은 반드시 **종료 조건**이 필요!!!!
- for과 차이점
    - for : iterable의 요소를 하나씩 순회하며 반복
        - 반복 횟수가 명확하게 정해져 있는 경우 유용
        - 예를 들어 리스트, 튜플, 문자열 등과 같은 시퀀스 형식의 데이터 처리시
    - while : 주어진 조건식이 참인 동안 반복
        - 반복 횟수가 불명확하거나 조건에 따라 반복을 종료해야 할 때 유용
        - 예를 들어 사용자의 입력을 받아서 특정 조건이 충족될 때까지 반복하는 경우

### 반복 제어

- for문과 while은 매 반복마다 본문 내 모든 코드를 실행하지만 때때로 일부만 실행하는 것이 필요할 때가 있음
- break : 반복을 즉시 중지
- continue : 다음 반복으로 건너뜀
    - 현재 반복문의 남은 코드를 다 건너뛰고 다음 반복으로 넘어간다!
- break와 continue 주의사항
    - 남용시 코드의 가독성을 저하시킬 수 있음
    - 특정한 종료 조건을 만들어 break을 대신하거나, if문을 사용해 continue처럼 코드를 건너 뛸 수 도 있음

## List Comprehension

- 간결하고 효율적인 리스트 생성 방법

    ```python
    [expression for 변수 in iterable]
    list(expression for 변수 in iterable)
    ```
    - `변수` 의 값이 `expression`에 들어가는 것이라고 생각하면 됨!
- if문도 활용하기

    ```python
    [expression for 변수 in iterable if 조건식]
    list(expression for 변수 in iterable if 조건식)
    ```

- comprehension을 사용하지 않는 것이 가독성이 더 좋음 → 남용 금지!!
    - but 속도는 더 빠름?

    ```python
    # comprehension
    result = [i for i in range(10) if i % 2 == 1]

    # no comprehension
    result = []
    for i in range(10):
        if i % 2 == 1:
            result.append(i)
    ```


## 참고

### pass

- 아무런 동작도 수행하지 않고 넘어가는 역할
- 문법적으로 문장이 필요하지만 프로그램 실행에는 영향을 주지 않아야 할 때 사용
- 예시
    1. 코드 작성 중 미완성 부분
        - 구현해야 할 부분이 나중에 추가될 수 있고, 코드를 컴파일하는 동안 오류가 발생하지 않음
        
        ```python
        def my_function():
        	pass
        ```
        
    2. 조건문에서 아무런 동작을 수행하지 않아야 할 때
        
        ```python
        if condition:
        	pass        # 아무런 동작도 수행하지 않음
        else:
        		            # 다른 동작 수행
        ```
        
    3. 무한 루프에서 조건이 충족되지 않을 때 pass를 사용하여 루프를 계속 진행하는 방법
        
        ```python
        while True:
        	if condition:
        		break
        	elif condition:
        		pass        # 루프 계속 진행
        	else:
        		print('..')
        ```
        
    
    ### enumerate
    
    - iterable 객체의 각 요소에 대해 인덱스와 함께 반환하는 내장함수
    - 인덱스와 요소가 튜플 형태로 반환됨
    - `enumerate(iterable, start = 0)`
    ```python
    fruits = ['apple', 'banana', 'cherry']

    for index, fruit in enumerate(fruits):
        print(f'인덱스 {index} : {fruit}')

    '''
    인덱스 0 : apple
    인덱스 1 : banana
    인덱스 2 : cherry
    '''
    ```