## Thread 활용

#### 스레드
> 하나의 작업단위

#### 멀티스레딩
> 하나의 프로세스 안에 여러개의 스레드가 동시에 작업을 수행하는 것

#### 스레드 구현
자바에서 스레드 구현 방법은 2가지가 있다.

1. Runnable 인터페이스 구현
```java
public class MyThread implements Runnable {
    @Override
    public void run() {
        // 수행 코드
    }
}
```

2. Thread 클래스 상속

```java
public class MyThread extends Thread {
    @Override
    public void run() {
        // 수행 코드
    }
}
```

#### 스레드 생성
1. 인터페이스로 구현한 경우
> 해당 클래스를 인스턴스화해서 Thread 생성자에 argument로 넘겨줘야 한다
```Java
public static void main(String[] args) {
    Runnable r = new MyThread();
    Thread t = new Thread(r, "mythread");
}
```

2. Thread 클래스를 상속받은 경우
> 상속받은 클래스 자체를 스레드로 사용할 수 있다
- Runnable 구현의 경우 Thread 클래스의 static 메소드인 currentThread()를 호출하여 현재 스레드에 대한 참조를 얻어와야만 호출이 가능하다.
```Java
public class ThreadTest implements Runnable {
    public ThreadTest() {}
    
    public ThreadTest(String name){
        Thread t = new Thread(this, name);
        t.start();
    }
    
    @Override
    public void run() {
        for(int i = 0; i <= 50; i++) {
            System.out.print(i + ":" + Thread.currentThread().getName() + " ");
            try {
                Thread.sleep(100);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}
```

#### 스레드 실행

> 스레드의 실행은 run() 호출이 아닌 start() 호출로 해야한다.
- start() 함수가 새로운 콜스택을 생성하기 때문


#### 동기화
>동기화는 시스템을 동시에 작동시키기 위해 여러 사건들을 조화시키는 것
- 여러 스레드가 같은 프로세스 내의 자원을 공유하면서 작업할 때 서로의 작업이 다른 작업에 영향을 주기 때문에 필요함

```Java
//synchronized : 스레드의 동기화. 공유 자원에 lock
public synchronized void saveMoney(int save){    // 입금
    int m = money;
    try{
        Thread.sleep(2000);    // 지연시간 2초
    } catch (Exception e){

    }
    money = m + save;
    System.out.println("입금 처리");

}

public synchronized void minusMoney(int minus){    // 출금
    int m = money;
    try{
        Thread.sleep(3000);    // 지연시간 3초
    } catch (Exception e){

    }
    money = m - minus;
    System.out.println("출금 완료");
}
```

> **참조**<br>
> &nbsp;&nbsp;[Java에서의 Thread](https://github.com/gyoogle/tech-interview-for-developer/blob/master/Language/%5Bjava%5D%20Java%EC%97%90%EC%84%9C%EC%9D%98%20Thread.md)
