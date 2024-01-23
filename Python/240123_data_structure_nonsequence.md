## 비시퀀스 데이터 구조

- 순서가 없어서 인덱스 접근이 불가능한 데이터들@!@!

### 세트(set)

- 고유한 항목들의 정렬되지 않은 컬렉션
    
    = 중복이 없는 비시퀀스
    

| 메서드 | 설명 |
| --- | --- |
| s.add(x) | 세트 s에 항목 x를 추가. 이미 x가 있다면 변화 없음 |
| s.clear() | 세트 s의 모든 항목을 제거 |
| s.remove(x) | 세트 s에서 항목 x를 제거. 항목 x가 없을 경우 Key error |
| s.pop() | 세트 s에서 랜덤하게 항목을 반환하고, 해당 항목을 제거 |
| s.discard(x) | 세트 s에서 항목 x를 제거. remove와 달리 에러 없음 |
| s.update(iterable) | 세트 s에 다른 iterable 요소를 추가 |

[예시 코드](./codes/set_method.py)

### 세트의 집합 메서드

| 메서드 | 설명 | 연산자 |
| --- | --- | --- |
| set1.difference(set2) | set1에는 들어있지만 set2에는 없는 항목으로 세트를 생성 후 반환 | set1 – set2 |
| set1.intersection(set2) | set1과 set2 모두 들어있는 항목으로 세트를 생성 후 반환 | set1 & set 2 |
| set1.issubset(set2) | set1의 항목이 모두 set2에 들어있으면 True를 반환 | set1 <= set2 |
| set1.issuperset(set2) | set1가 set2의 항목을 모두 포함하면 True를 반환 | set1 >= set2 |
| set1.union(set2) | set1 또는 set2에(혹은 둘 다) 들어있는 항목으로 세트를 생성 후 반환 | set1 | set2 |


[예시 코드](./codes/set_method2.py)


### 딕셔너리

- 고유한 항목들의 정렬되지 않은 컬렉션

| 메서드 | 설명 |
| --- | --- |
| D.clear() | 딕셔너리 D의 모든 키/값 쌍을 제거 |
| D.get(k) | 키 k에 연결된 값을 반환 (키가 없으면 None을 반환) |
| D.get(k, v) | 키 k에 연결된 값을 반환하거나 키가 없으면 기본 값으로 v를 반환 |
| D.keys() | 딕셔너리 D의 키를 모은 객체를 반환 |
| D.values() | 딕셔너리 D의 값을 모은 객체를 반환 |
| D.items() | 딕셔너리 D의 키/값 쌍을 모은 객체를 반환 |
| D.pop(k) | 딕셔너리 D에서 키 k를 제거하고 연결됐던 값을 반환 (없으면 오류) |
| D.pop(k, v) | 딕셔너리 D에서 키 k를 제거하고 연결됐던 값을 반환 (없으면 v를 반환) |
| D.setdefault(k) | 딕셔너리 D에서 키 k와 연결된 값을 반환 |
| D.setdefault(k, v) | 딕셔너리 D에서 키 k와 연결된 값을 반환<br>k가 D의 키가 아니면 값 v와 연결한 키 k를 D에 추가하고 v를 반환 |
| D.update(other) | other 내 각 키에 대해 D에 있는 키면 D에 있는 그 키의 값을 other에 있는 값으로 대체.<br>other에 있는 각 키에 대해 D에   없는 키면 키/값 쌍을 D에 추가 |

[예시 코드](./codes/dict_method.py)