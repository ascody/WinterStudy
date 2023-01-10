## Garbage Collection

### Garbage Collection(가비지 컬렉션)이란
> 사용하지 않는 객체를 자동으로 해제하는 기능<br>
  -> 힙(Heap) 영역의 메모리를 정리

### 가비지 컬렉션의 대상

1. 객체가 NULL인 경우 (ex. String str = null)

2. 블럭 실행 종료 후, 블럭 안에서 생성된 객체

3. 부모 객체가 NULL인 경우, 포함하는 자식 객체

### 약한 세대 가설(Weak Generational Hypothesis)

> JVM의 Heap영역이 처음 설계될 때 설정한 2가지 전제

1. 대부분의 객체는 금방 접근 불가능한 상태(Unreachable)가 된다.

2. 오래된 객체에서 새로운 객체로의 참조는 아주 적게 존재한다.

   => **객체는 대부분 일회성되며, 메모리에 오랫동안 남아있는 경우는 드묾**

**객체의 생존 기간에 따라 물리적인 Heap 영역을 나누게 되었고 Young, Old 총 2가지 영역으로 설계**

#### Young 영역(Young Generation)

 - 새롭게 생성된 객체가 할당(Allocation)되는 영역

 - 많은 객체가 Young 영역에 생성되었다가 사라짐

 - Young 영역에 대한 가비지 컬렉션을 **Minor GC** 라고 함

#### Old 영역(Old Generation)

 - Young영역에서 Reachable 상태를 유지하여 살아남은 객체가 복사되는 영역

 - Young 영역보다 크게 할당되며, 영역의 크기가 큰 만큼 가비지는 적게 발생

 - Old 영역에 대한 가비지 컬렉션을 **Major GC 또는 Full GC** 라고 함

### 동작 방식

#### Stop the World

> 가비지 컬렉션을 실행하기 위해 JVM이 애플리케이션의 실행을 멈추는 작업

-  GC를 실행하는 쓰레드를 제외한 모든 쓰레드들의 작업이 중단

-  GC가 완료되면 작업이 재개

#### Mark and Sweep

> Mark : 사용되는 메모리와 사용되지 않는 메모리를 식별하는 작업<br>
> Sweep : Mark 단계에서 사용되지 않음으로 식별된 메모리를 해제하는 작업

- 스택의 모든 변수 또는 Reachable 객체를 스캔하면서 각각이 어떤 객체를 참고하고 있는지를 탐색

- 사용되고 있는 메모리를 식별(Mark)

- Mark가 되지 않은 객체들을 메모리에서 제거(Sweep)

#### Minor GC

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FCyho2%2FbtqURvZRql6%2F4a7u6mMGofkpuURKQz0RT1%2Fimg.png)

> Young 영역에 대한 가비지 컬렉션

- 1개의 Eden 영역과 2개의 Survivor 영역

- Eden 영역: 새로 생성된 객체가 할당(Allocation)되는 영역

- Survivor 영역: 최소 1번의 GC 이상 살아남은 객체가 존재하는 영역

1. 새로 생성된 객체가 Eden 영역에 할당

2. 객체가 계속 생성되어 Eden 영역이 꽉차게 되고 Minor GC가 실행

   1. Eden 영역에서 사용되지 않는 객체의 메모리가 해제

   2. Eden 영역에서 살아남은 객체는 1개의 Survivor 영역으로 이동

3. Survivor 영역이 가득 차게 되면 Survivor 영역의 살아남은 객체를 다른 Survivor 영역으로 이동

3. 이러한 과정을 반복하여 계속해서 살아남은 객체는 Old 영역으로 이동

#### Major GC

> Old 영역에 대한 가비지 컬렉션

* Young 영역에서 오래 살아남은 객체는 Old 영역으로 Promotion

* Major GC는 객체들이 계속 Promotion되어 Old 영역의 메모리가 부족해지면 발생

* Old 영역은 Young 영역보다 크며 Young 영역을 참조할 수도 있음

* Major GC는 일반적으로 Minor GC보다 시간이 오래걸리며, 10배 이상의 시간을 사용

> **참조**<br>
> [tech-interview-for-developer](https://github.com/GimunLee/tech-refrigerator/blob/master/Language/JAVA/Garbage%20Collection.md#garbage-collection)<br>
> [[Java] Garbage Collection(가비지 컬렉션)의 개념 및 동작 원리 (1/2)](https://mangkyu.tistory.com/118)<br>
> [JVM의 Garbage Collection](https://www.holaxprogramming.com/2013/07/20/java-jvm-gc/)
