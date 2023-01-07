## Casting(업캐스팅 & 다운캐스팅)

<img src = "https://www.scaler.com/topics/images/upcasting-and-downcasting-in-java-thumbnail.webp" width="35%" height="35%">

### 캐스팅(Casting)이란
> **하나의 데이터 타입을 다른 타입으로 바꾸는 것**

- 대입 연산자 `=` 에서 변수 와 값 서로 양쪽의 타입이 일치하지 않으면 할당이 불가능
- 그래서 다음과 같이 강제적으로 타입을 지정할 수 있음

```c
int i = (int)10.233; // 명시적 형변환
double d = 12; // 묵시적 형변환
```

### 참조변수에서의 형변환

> 사용할 수 있는 **멤버의 갯수를 조절**

### 업캐스팅(UpCasting)

> 자식 클래스가 부모 클래스 타입으로 캐스팅 되는 것

- 업캐스팅은 캐스팅 연산자 괄호를 생략 가능

- 부모 클래스로 캐스팅 된다는 것은 멤버의 갯수 감소를 의미<br>

  -> 자식 클래스만 갖고 있는 필드와 메소드는 **사용할 수 없음**

- 오버라이딩한 메서드가 있을 경우, 부모 클래스의 메서드가 아닌 **오버라이딩 된 메서드**가 실행

#### 업캐스팅을 사용하는 이유

> **공통적으로 할 수 있는 부분을 만들어 간단하게 다루기 위해서**

- 상속 관계에서 상속 받은 서브 클래스가 몇 개이든 하나의 인스턴스로 묶어 관리할 수 있음
```Java
  // Shape 의 자식 클래스 Triangle, Rectangle, Circle를 Shape로 묶어 관리
  Shape[] s = new Shape[3];
  s[0] = new Triangle();
  s[1] = new Rectangle();
  s[2] = new Circle();
```

### 다운캐스팅(DownCasting)

> 부모 클래스가 자식 클래스 타입으로 캐스팅 되는 것

- 캐스팅 연산자 괄호를 생략 불가

- **업캐스팅한 객체를 다시 자식 클래스 타입의 객체로 되돌리는 것이 목적 (복구)**

- **업캐스팅의 반대 개념이 아님**

- 부모 클래스로 업 캐스팅된 자식 클래스를 복구하여, 본인의 원래 있던 기능을 회복하기 위함

```C#
  Shape shape_up;
  Triangle triangle = new Triangle();
  shape = triangle;
  
  // 자식만 있는 멤버를 이용하기 위해 다운캐스팅
  Triangle shape_down = (Triangle)shape;
  shape_down.semo();
```

#### 주의점

- 부모객체를 다운캐스팅 하면 오류(ClassCastException)가 발생
- 형제 클래스 끼리는 서로 캐스팅이 불가능 (업캐스팅도 마찬가지)
- 잘못 다운캐스팅 시 컴파일 에러가 발생하기 않고 런타임 에러가 발생하는 위험성이 있음

> **참조**<br>
> [[JAVA] ☕ 업캐스팅 & 다운캐스팅 - 완벽 이해하기](https://inpa.tistory.com/entry/JAVA-%E2%98%95-%EC%97%85%EC%BA%90%EC%8A%A4%ED%8C%85-%EB%8B%A4%EC%9A%B4%EC%BA%90%EC%8A%A4%ED%8C%85-%ED%95%9C%EB%B0%A9-%EC%9D%B4%ED%95%B4%ED%95%98%EA%B8%B0#%EC%97%85%EC%BA%90%EC%8A%A4%ED%8C%85(UpCasting))<br>
> [[Java] 업캐스팅과 다운캐스팅](https://velog.io/@smallcherry/Java-UpCastingAndDownCasting)
