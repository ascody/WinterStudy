## JAVA Stream

### Stream API
> 람다를 사용한 함수형 프로그래밍
- 8버전 이상부터 지원함

### Collection vs Stream

#### Colection
> 데이터의 집합, 그룹
- 자료구조가 포함하는 모든 값을 메모리에 저장
- 컬렉션의 모든 요소는 컬렉션에 추가하기 전에 계산되어야 함 (모든 값을 계산할 때까지 기다림)

#### Stream
> 데이터 처리연산을 지원하도록 소스에서 추출된 연속된 요소
- 고정된 자료구조 (요소 추가,제거 불가능)
- 사용자가 요청하는 값만 스트림에서 추출 (필요할 때만 값을 계산)
- 탐색된 소비된 스트림의 요소는 소비됨

#### 외부 반복
> for-each 등을 사용해서 직접 요소를 반복
- 컬렉션은 외부 반복을 사용
- 명시적으로 항목을 하나씩 처리

#### 내부 반복
> 반복을 자동으로 처리
- 스트림은 내부 반복을 사용
- 반복을 숨겨주는 연산 리스트가 정의되어 있어야 함
- 반복을 숨겨주는 연산은 대부분 람다 표현식으로 인수를 받음

### Stream 연산

#### Stream 중간 연산

> 파이프라이닝이 가능한 연산

- 스트림을 반환함
 
**filter(Predicate)   
distinct()   
limit(n)   
skip(n)   
map(Function)   
flatMap()**

#### Stream 최종 연산

> 스트림을 닫는 연산

- 최종값을 반환함
 
**(boolean) allMatch(Predicate)   
(boolean) anyMatch(Predicate)   
(boolean) noneMatch(Predicate)   
(Optional) findAny()   
(Optional) findFirst()   
reduce()   
collect()   
(void) forEach()   
(Long) count**

> **참조**<br>
> [JAVA Stream](https://github.com/gyoogle/tech-interview-for-developer/blob/master/Language/%5Bjava%5D%20Stream.md)<br>
> [Java - Stream 이란? (Stream과 Collection, Stream 각 연산)](https://galid1.tistory.com/674)<br>
> [[모던자바인액션] 컬렉션과 스트림의 차이점(Stream vs Collection)](https://ssyoni.tistory.com/11)<br>
