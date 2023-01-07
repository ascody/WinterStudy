## 오토 박싱 & 오토 언박싱

### 래퍼 클래스 (Wrapper Class)
![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fbvzp79%2FbtqEbacB01v%2FQQjO7cSc9tTvKJkyzFsK90%2Fimg.png)
> 기본 자료타입(primitive type)을 객체로 다루기 위해서 사용하는 클래스

|기본타입(primitive type)|래퍼클래스(wrapper class)|
| ----------------------- | -----------------------|
|byte|Byte|
|char|Character|
|int|Integer|
|float|Float|
|double|Double|
|boolean|Boolean|
|long|Long|
|short|Short|

### 박싱(Boxing) & 언박싱(UnBoxing)

> 박싱 : 기본타입의 값을 래퍼클래스로 변환

> 언박싱 : 래퍼클래스에서 기본타입으로 변환

### 오토 박싱 & 오토 언박싱

> 래퍼클래스 타입에 기본값이 대입될 경우 자동으로 박싱

> 기본타입에 래퍼클래스 값이 대입될 경우 자동으로 언박싱

```Java
public class Wrapper_Ex {
    public static void main(String[] args)  {
        Integer num = 17; // 자동 박싱
        int n = num; //자동 언박싱
    }
}
```
### 성능

- 자동으로 일어나지만 추가 연산 작업이 발생

- 웬만하면 동일 타입 연산으로 구현하는 것이 좋음

#### 오토 박싱 연산
![](https://github.com/ascody/WinterStudy/blob/main/Java/%EC%98%A4%ED%86%A0%EB%B0%95%EC%8B%B1.png?raw=true)

#### 동일 타입 연산
![](https://github.com/ascody/WinterStudy/blob/main/Java/%EB%8F%99%EC%9D%BC%ED%83%80%EC%9E%85.png?raw=true)

**-> 동일 타입 연산이 5배 가량 빠름**

> **참조**<br>
> [[Java] 래퍼 클래스(Wrapper Class)란 무엇인가? (박싱, 언박싱)](https://coding-factory.tistory.com/547)
