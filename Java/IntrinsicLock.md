## Java 고유 락 (Intrinsic Lock)

### 락(Lock)
> 멀티스레딩 환경에서 동기화를 진행하기 위한 기초적인 장치

### 고유 락 (Intrinsic Lock)

> Java의 모든 객체는 lock을 갖고 있어 이를 고유 락이라고 부름

- 모니터 락(monitor lock) 혹은 그냥 모니터(monitor)라고도 함

- Synchronized 블록은 Intrinsic Lock을 이용해서, Thread의 접근을 제어함.<br>
   -> Synchronized 블록은 객체 단위로 Lock을 다룸

### Thread-safe Case

- 아래와 같은 연산은 서로 다른 쓰레드에서 동시에 변수에 접근 가능함

```java
public class Counter {
    private int count;
 
    public int increase() {
        return ++count;		// Thread-safe 하지 않은 연산
    }
}
```

- lock이라는 Object의 instance를 사용하여 스레드가 동시에 count 변수에 접근하지 못하도록 제어함

```java
 public class Counter {
   private Object lock = new Object();
   private int count;

   public int increase() {
     synchronized(lock) {
       return ++count;
     }
   }
 }
```

- synchronized 키워드를 붙여주는 것으로 대신할 수 있음

```java
public class Counter {
  private int count;

  public synchronized int increase() {
    return ++count;
  }
}
```

### 재진입성 (Reentrancy)

> 둘 이상의 스레드에 의해 호출되었을 때 호출된 순서에 상관없이 제대로 된 결과를 반환하는 것

> Lock을 획득한 Thread가 같은 Lock을 얻기 위해 대기할 필요가 없는 것<br>
  -> Lock의 획득이 호출 단위가 아닌 **Thread 단위**로 일어남

```java
public class Reentrancy {
    public synchronized void a() {
        System.out.println("a");
        b();
    }

    public synchronized void b() {
        System.out.println("b");
    }

    public static void main (String[] args) {
        new Reentrancy().a();
    }
}
```
- 만약 자바의 고유 락이 재진입 가능하지 않다면 위 코드는 a 메서드 내부의 b를 호출하는 지점에서 [데드락](https://chanhuiseok.github.io/posts/cs-2/)이 발생함

### 구조적인 락 (structured lock)

> 고유 락을 이용한 동기화

- synchronized 블록 단위로 락의 획득/해제가 일어나므로 구조적이라 함

- synchronized 블록을 **진입**할 때 락의 **획득**이 일어나고, 블록을 **벗어날 때** 락의 **해제**가 일어남

- A 획득 -> B 획득 -> B 해제 -> A 해제는 가능

- A 획득 -> B 획득 -> A 해제 -> B 해제는 불가능

- 위 순서대로 락을 사용하려면 명시적인 락(ReentrantLock)을 사용해야함

### 가시성 (Visibility)
> 여러 Thread가 동시에 작동하였을 때, 한 Thread가 쓴 값을 다른 Thread가 볼 수 있는지, 없는지 여부

- Structure Lock과 Reentrant Lock은 Visibility를 보장

#### 가시성 문제

> 한 스레드가 쓴 값을 다른 스레드가 볼 수 없을 때 발생하는 문제

- 가시성을 보장해야 항상 업데이트된 값을 사용 가능

- 원인
  - 최적화를 위해 Compiler나 CPU에서 발생하는 코드 재배열
  - CPU core의 cache 값이 Memory에 제때 쓰이지 않아 발생

> **참조**<br>
> [Java 고유 락 (Intrinsic Lock)](https://github.com/gyoogle/tech-interview-for-developer/blob/master/Language/%5BJava%5D%20Intrinsic%20Lock.md)<br>
> [<CS 지식> Java 고유락 (Intrinsic Lock)](https://velog.io/@kimmy/CS-%EC%A7%80%EC%8B%9D-Java-%EA%B3%A0%EC%9C%A0%EB%9D%BD-Intrinsic-Lock)<br>
> [Java의 고유 락(intrinsic lock)에 대해](http://happinessoncode.com/2017/10/04/java-intrinsic-lock/)<br>
> [함수, 서브루틴의 재진입성(Reentrant)이란? Thread-safe와 reentrancy](https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=complusblog&logNo=220985740336)
