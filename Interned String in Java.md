## Interned String in Java

### 문자열 선언 방식

1. new 연산자를 이용하는 방법

```java
String str = new String("Hello");
```

2. 리터럴을 이용하는 방법 

```java
String str = "Hello";
```

### 문자열 간 비교

```java
public void func() {
    String haribo1st = new String("HARIBO");
    String haribo3rd = "HARIBO";

    System.out.println(haribo1st == haribo3rd); // false
    System.out.println(haribo1st.equals(haribo3rd)); // true
}
```

- 생성자를 통해 선언하게 되면 같은 문자열을 가진 새로운 객체가 생성

- 서로 주소가 다르게 됨

<br>

```java
public void func() {
    String haribo3rd = "HARIBO";
    String haribo4th = String.valueOf("HARIBO"); // 리터럴
        
    System.out.println(haribo3rd == haribo4th); // true
    System.out.println(haribo3rd.equals(haribo4th)); // true
}
```

- 리터럴 선언을 한 문자열은 서로 주소가 같음

### intern()

> 리터럴 문자열 생성 시 호출되는 메소드

- 리터럴을 이용할 경우 문자열은 `string contstant pool`이라는 영역에 존재

-  intern() 메서드는 주어진 문자열이 string constant pool에 존재하는지 검색하고 있다면 그 주소값을 반환, 없다면 string constant pool에 넣고 새로운 주소값을 반환


> **참조**<br>
> [Interned String in Java](https://github.com/gyoogle/tech-interview-for-developer/blob/master/Language/%5BJava%5D%20Interned%20String%20in%20JAVA.md)<br>
> [[JAVA] String 객체와 리터럴 (메모리관련)](https://cornswrold.tistory.com/253)
