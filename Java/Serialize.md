![](https://hazelcast.com/wp-content/uploads/2021/12/serialization-deserialization-diagram-800x318-1.png)

## Serialize

### 직렬화(Serialize)
> 자바 시스템 내부에서 사용되는 Object 또는 Data를 외부의 자바 시스템에서도 사용할 수 있도록 byte 형태로 데이터를 변환하는 기술

- 객체를 데이터스트림으로 만드는것

- JVM(Jaava Virtual Machine 이하 JVM)의 메모리에 상주(힙 또는 스택)되어 있는 객체 데이터를 바이트 형태로 변환

#### 장점

- 객체 데이터를 그대로 영속화(persist)가 필요할 때 사용

- 파일형태로 저장되어 네트워크를 통해 전송이 가능

- 역직렬화 할 경우 기존 객체처럼 사용이 가능

#### 직렬화 대상

- `java.io.Serializable` 인터페이스를 상속받은 객체 

- Primitive 타입 데이터

#### 직렬화 방법

- `java.io.ObjectOutputStream` 를 사용하여 직렬화를 진행

```java
public static void main(String[] args){
    Member member = new Memer("김배민", "deliverykim@baemin.com", 25);
    byte[] serializeMember;
    try(ByeArrayOutputStream baos= new ByteArrayOutputStream()){
        try(ObjectOutputStream oos= new ObjectOutputStream(baos)){
            oos.writeObject(member);
            // serializedMember -> 직렬화된 member 객체
            serializedMember = baos.toByteArray();
        }
    }
  //바이트 배열로 생성된 직렬화 데이터를 base64로 변환
  System.out.println(Base64.getEncoder().encodeToString(serializedMember));
}
public class Member implements Serializable {
    private String name;
    private String email;
    private int age;

    public Member(String name, String email, int age) {
        this.name = name;
        this.email = email;
        this.age = age;
    }

    // Getter 생략

    @Override
    public String toString() {
        return String.format("Member", name, email, age);
    }
}
```

<br>

### 역직렬화(Deserialize)
> 바이트로 변환된 데이터를 다시 객체로 변환하는 기술

#### 역직렬화 조건

- 직렬화 대상이 된 객체의 클래스가 클래스 패스에 존재해야하며 import 되어 있어야 함

- 자바 직렬화 대상 객체는 동일한 serialVersionUID 를 가지고 있어야 함 (자동으로 생성됨)
```java
private static final long serialVersionUID= 1L;
```

#### 역직렬화 방법

- `java.io.ObjectInputStream` 를 사용하여 역직렬화를 진행

```java
public static void main(String[] args){
  //직렬화 예제에서 생성된 base64 데이터
  String base64Member="...생략";
  byte[] serializedMember = Base64.getDecoder().decode(base64Member);
  try(ByteArrayInputStream bais = new ByteArrayInputStream(serializedMember)){
    try(ObjecInputStream ois = new ObjectInputStream(bais)){
      //역직렬화된 member객체를 읽어온다.
      Object objectMember = ois.readObject();
      Member member = (Member)objectMember;
      System.out.println(member);
    }
  }
}
```

<br>

### serialVersionUID
> Java 직렬화 및 역직렬화 할때 필요한 버전 정보

- 호환 가능한 클래스는 serialVersionUID 값이 고정

- serialVersionUID가 선언되어 있지 않으면 클래스의 기본 해쉬값을 사용

- **변경에 취약한 클래스가 변경되면 역직렬화 시에 예외가 발생할 수 있음**

- 기존의 직렬화된 객체의 멤버 변수의 타입이 바뀐다면 마찬가지로 `java.io.InvalidClassException` 예외가 발생

- **serialVersionUID 값은 직접 관리해주는 것이 좋음**

<br>

### 직렬화를 사용하는 경우

- 서블릿 세션 (Servlet Session)
> 웹 서버에서 파일로 저장하거나 세션 클러스터링, DB를 저장하는 옵션을 선택하는 경우

- 캐시 (Cache)
> 저장소를 이용해서 데이터 객체를 저장한 후 동일한 요청이 오면 DB를 다시 요청하는 것이 아니라 저장된 객체를 찾아서 응답하게 함

- [자바 RMI(Remote Method Invocation)](https://docs.oracle.com/javase/tutorial/rmi/index.html)
> 원격 시스템 간의 메시지 교환에서 시스템의 메서드를 호출 시에 전달하는 메시지(보통 객체)를 자동으로 직렬화


> **참조**<br>
> [[Java] 직렬화(Serialization)](https://github.com/gyoogle/tech-interview-for-developer/blob/master/Language/%5BJava%5D%20%EC%A7%81%EB%A0%AC%ED%99%94(Serialization).md#java-%EC%A7%81%EB%A0%AC%ED%99%94serialization)<br>
> [자바 직렬화, 그것이 알고싶다. 훑어보기편](https://techblog.woowahan.com/2550/)<br>
> [Java의 직렬화(Serialize)란?](https://go-coding.tistory.com/101)<br>
> [Serialize란 무엇인가?](https://ahma.tistory.com/65)<br>
> [Java 직렬화를 하는 이유가 무엇일까?](https://velog.io/@sa1341/Java-%EC%A7%81%EB%A0%AC%ED%99%94%EB%A5%BC-%ED%95%98%EB%8A%94-%EC%9D%B4%EC%9C%A0%EA%B0%80-%EB%AC%B4%EC%97%87%EC%9D%BC%EA%B9%8C)
