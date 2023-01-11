## Record

### 레코드 (Record)
> 불변(immutable) 데이터 객체를 쉽게 생성할 수 있도록 하는 새로운 유형의 클래스
- JDK14에서 preview로 등장하여 JDK16에서 정식 스펙으로 포함

### 기존의 불변 데이터 객체

- 많은 코드의 작성이 필요함

```java
public class Person {
    private final String name;
    private final int age;
    
    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }
    
    public String getName() {
        return name;
    }
    
    public int getAge() {
        return age;
    }
}
```

### 레코드를 이용한 불변 객체

- 컴파일러는 헤더를 통해 내부 필드를 추론

- 생성자, getter, equals, hashCode, toString 등의 메소드를 자동으로 생성

```java
public record Person(String name, int age) {
}
```

### 레코드의 제한

- 레코드는 암묵적으로 final 클래스(상속불가)이고, abstract 선언 불가

- 다른 클래스를 상속(extends) 받을 수 없음, 인터페이스 구현(implements)은 가능

> **참조**<br>
> [[Java] Record](https://github.com/gyoogle/tech-interview-for-developer/blob/master/Language/%5Bjava%5D%20Record.md) <br>
> [[Java] 자바의 레코드(Record)](https://scshim.tistory.com/372) <br>
