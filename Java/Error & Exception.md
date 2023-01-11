## Error & Exception

### 오류 (Error)
> 시스템이 종료되어야 할 수준과 같이 수습할 수 없는 심각한 문제

ex) `StackOverflowError`, `OutOfMemoryError`

### 예외 (Exception)
> 개발자가 구현한 로직에서 발생한 실수나 사용자의 영향에 의해 발생하는 문제

- 개발자가 미리 예측하여 방지할 수 있다.

ex) `NullPointerException`, `IllegalAccessException`

<br>

![](https://madplay.github.io/img/post/2019-03-02-java-checked-unchecked-exceptions-1.png)

#### Checked Exception
> RuntimeException을 상속하지 않는 예외
- 컴파일 시점에서 체크
- 발생하면 컴파일되지 않음 <br>-> 반드시 예외처리
ex) `IOException`, `SQLException`

#### Unchecked Exception
> RuntimeException을 상속받는 예외
- 런타임 시점에서 체크
- 예외 발생 시 롤백해야 함
ex) `NullPointerException`, `IndexOutOfBoundException`

### 예외처리 방법

#### 예외 복구
> 예외 상황을 파악하고 문제를 해결해서 정상 상태로 돌려놓는 방법

- 예외를 잡아서 일정 시간, 조건만큼 대기하고 다시 재시도를 반복

- 최대 재시도 횟수를 넘기게 되는 경우 예외를 발생

```java
final int MAX_RETRY = 100;
public Object someMethod() {
    int maxRetry = MAX_RETRY;
    while(maxRetry > 0) {
        try {
            ...
        } catch(SomeException e) {
            // 로그 출력. 정해진 시간만큼 대기한다.
        } finally {
            // 리소스 반납 및 정리 작업
        }
    }
    // 최대 재시도 횟수를 넘기면 직접 예외를 발생시킨다.
    throw new RetryFailedException();
}
```

#### 예외 회피
> 예외 처리를 직접 담당하지 않고 호출한 쪽으로 던져 회피하는 방법

- 어느 정도 처리 후 보내는 것이 좋음

- 긴밀한 역할 관계가 아니면 지양해야 함

```java
// 예시 1
public void add() throws SQLException {
    // ...생략
}

// 예시 2 
public void add() throws SQLException {
    try {
        // ... 생략
    } catch(SQLException e) {
        // 로그를 출력하고 다시 날린다!
        throw e;
    }
}
```

#### 예외 전환
> 예외 회피와 비슷하게 메서드 밖으로 예외를 던지지만, 그냥 던지지 않고 적절한 예외로 전환해서 넘기는 방법

- 조금 더 명확한 의미로 전달되기 위해 적합한 의미를 가진 예외로 변경

- 예외 처리를 단순하게 만들기 위해 포장(wrap) 할 수도 있음

```java
// 조금 더 명확한 예외로 던진다.
public void add(User user) throws DuplicateUserIdException, SQLException {
    try {
        // ...생략
    } catch(SQLException e) {
        if(e.getErrorCode() == MysqlErrorNumbers.ER_DUP_ENTRY) {
            throw DuplicateUserIdException();
        }
        else throw e;
    }
}

// 예외를 단순하게 포장한다.
public void someMethod() {
    try {
        // ...생략
    }
    catch(NamingException ne) {
        throw new EJBException(ne);
        }
    catch(SQLException se) {
        throw new EJBException(se);
        }
    catch(RemoteException re) {
        throw new EJBException(re);
        }
}
```

> **참조**<br>
> [Error & Exception](https://github.com/GimunLee/tech-refrigerator/blob/master/Language/JAVA/Error%20%26%20Exception.md#error--exception)<br>
> [[Java] Error와 Exception](https://choiblack.tistory.com/39)<br>
> [자바 예외 구분: Checked Exception, Unchecked Exception](https://madplay.github.io/post/java-checked-unchecked-exceptions)<br>
> [java 예외 처리(Exception 처리)](https://www.leafcats.com/181)
