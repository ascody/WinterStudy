<img src="https://i.ytimg.com/vi/VfTiLE3RZds/maxresdefault.jpg" width=70%>

## Composition

### 상속(Inheritance)
> 다른 객체를 물려받아 그 객체의 요소를 사용하는 것

- IS-A관계로 정의될 수 있으며, 부모클래스를 '확장'하는 개념이다.

- 상속(클래스→클래스)의 단점

  * 부모 객체의 수정이 자식 객체에게도 영향을 줌(캡슐화를 위반)

  * 부모 객체의 메소드에 설계가 영향을 받음(유연하지 못한 설계)

  * 다중상속 불가능함

  * 오버라이드 시 부모 객체의 내부 구조를 알아야 함

### 컴포지션(Composition, 조합)
> 다른 객체의 인스턴스를 자신의 인스턴스 변수로 포함해서 메서드를 호출하는 기법

- HAS-A 관계로 정의될 수 있으며, 기존 클래스가 새로운 클래스의 구성요소가 되는 것

- 상속의 단점을 해결함

- 상속처럼 기존의 클래스를 확장(extend)하는 것이 아닌, 새로운 클래스를 생성하여 private 필드로 기존 클래스의 인스턴스를 참조하는 방식

- 어떠한 생성 작업이 일어나더라도 기존의 클래스는 전혀 영향을 받지 않음

- 예시 코드

```java
public class ForwardingSet<E> implements Set<E> {
    private final Set<E> set;
    public ForwardingSet(Set<E> set) { this.set = set; }
    public void clear() { set.clear(); }
    public boolean isEmpty() { return set.isEmpbty(); }
    public boolean add(E e) { return set.add(e); }
    public boolean addAll(Collection<? extends E> c) { return set.addAll(c); }
    // ... 생략
}
```

### 컴포지션의 장점

- 필요한 객체의 내부 구현을 이해할 필요 없음

- 캡슐화를 위반하지 않음

### 상속이 적절하게 사용되기 위한 조건

1. 확장을 고려하고 설계한 확실한 is - a 관계일 때

2. API에 아무런 결함이 없는 경우, 결함이 있다면 하위 클래스까지 전파돼도 괜찮은 경우

> **참고**<br>
> [[Java] 컴포지션(Composition)](https://github.com/gyoogle/tech-interview-for-developer/blob/master/Language/%5BJava%5D%20%EC%BB%B4%ED%8F%AC%EC%A7%80%EC%85%98(Composition).md)<br>
> [상속과 컴포지션](https://hpotter1993.tistory.com/36)<br>
> [컴포지션(Composition)](https://resucito.tistory.com/11)<br>
> [상속보다는 조합(Composition)을 사용하자.](https://tecoble.techcourse.co.kr/post/2020-05-18-inheritance-vs-composition/)
