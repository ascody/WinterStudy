<h2>String, StringBuffer, StringBuilder</h2>

| 분류   | String    | StringBuffer                    | StringBuilder        |
| ------ | --------- | ------------------------------- | -------------------- |
|&nbsp;&nbsp;변경| Immutable | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Mutable|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Mutable    |
| 동기화 |           | Synchronized 가능 (Thread-safe) | Synchronized 불가능. |

> 참고 : (https://ifuwanna.tistory.com/221)[https://ifuwanna.tistory.com/221]

### String vs StringBuffer / StringBuilder

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Ft1.daumcdn.net%2Fcfile%2Ftistory%2F99948B355E2F13350F)
![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Ft1.daumcdn.net%2Fcfile%2Ftistory%2F9923A9505E2F133608)

 - **차이점은 불변성**
 - 문자열 연산시 새로 객체를 만드는 Overhead 발생
 - 문자열 변경 시 기존 문자열은 Garbage Collector로 제거되어야 함
 - String은 문자열 추가,수정,삭제 등의 연산이 빈번하게 발생하는 환경에서 비효율적
 - StringBuffer, StringBuilder는 동일 객체 내에서 문자열 변경

### StringBuffer vs StringBuilder

 - **차이점은 동기화의 유무**
 - **StringBuffer**는 동기화 키워드를 지원하여 **멀티쓰레드** 환경에서 안전
 - **StringBuilder**는 동기화를 지원하지 않지만 **단일쓰레드**에서의 성능은 StringBuffer 보다 뛰어남

### 정리

**String** : 문자열 연산이 적고 조회가 많은 멀티쓰레드 환경

**StringBuffer** : 문자열 연산이 많은 멀티쓰레드 환경

**StringBuilder** : 문자열 연산이 많은 단일쓰레드 환경이거나 동기화를 고려하지 않아도 되는 경우  
