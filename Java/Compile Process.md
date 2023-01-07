![](https://goodgid.github.io/assets/img/java/Java-JVM_1.png)
<h2>자바 컴파일과정</h2>

### 컴파일 (Compile)

자바 컴파일러가 **자바 소스코드(.java)** 를 **자바 바이트 코드(.class)** 로 변환하고 클래스로더에 전달

> **자바 바이트 코드(Java bytecode)** : 자바 가상 머신이 이해할 수 있는 언어로 변환된 자바 소스코드

<br>

### 클래스 로더 (Class Loader)

동적로딩(Dynamic Loading)을 통해 **필요한 클래스**들을 **런타임**(바이트 코드를 실행할 때)에 로드하고 링크

   - 런타임 데이터 영역(Runtime Data area), 즉 **JVM의 메모리에 올림**

   - **로딩 -> 링크 -> 초기화**의 순서로 진행


#### 로딩(loading)

> .class 파일을 읽고 그 내용에 따라 적절한 **바이너리 데이터를 만들고 Method 영역에 저장**

- Method 영역에 저장하는 데이터
  - **Type 정보**
  - **메소드와 클래스 변수**(=Static변수)
  - **Fully Qualified Class Name**(클래스가 속한 패키지명을 모두 포함한 이름)

- 로딩이 끝나면 해당 Class Type의 Class 객체를 생성하여 힙 영역에 저장
- 클래스 로더의 종류는 **Bootstrap, Extension, Application** 3가지
- **Bootstrap -> Extension -> Application** 순으로 구동

   - *Bootstrap ClassLoader*
 : 최상위 클래스로더로, JVM 을 구동시키기 위한 가장 필수적인 라이브러리의 클래스들을 JVM 에 탑재

   - *Extension ClassLoader*
 : 표준 핵심 Java Class 의 라이브러리들을 JVM 에 탑재

   - *Application ClassLoader*
 : 개발자들이 자바 코드로 짠 클래스 파일들을 JVM 에 탑재


#### 링크(linking)

> 로드된 클래스나 인터페이스, 그 직계 부모클래스나 인터페이스를 검증하고, 준비하고, 해석하는 과정

- 링크 작업은 **Verify -> Prepare -> Resolve** 3단계

   - *Verify(검증)*
class 파일 형식이 자바 언어 명세(Java Language Specification) 및 JVM 명세에 명시된 대로 구성되어 있는지 검사

   - *Prepare(준비)*
 : 클래스 변수(static 변수)와 기본값에 필요한 메모리를 할당 (필드, 메서드, 인터페이스 등등)

   - *Resolve(분석)*
 : 클래스의 상수 풀 내 모든 심볼릭 레퍼런스를 다이렉트 레퍼런스로 변경<br>
  -> 참조변수를 heap에 저장된 인스턴스와 연결하는 과정


#### 초기화(initialization)

> static으로 선언된 변수와 메소드에 메모리를 할당해 초기값을 채우는 과정

<br>

**# 클래스 로더를 알아야 하는 이유**

- **was에 내가 만든 웹앱이 올라가는 경우**
- 클래스로더에 메모리를 올리면 프로그램 종료 이외에는 클래스 정보를 지우는 방법이 따로 없음.<br>
  -> 코드를 수정해서 재배포하기 어려움 <br>
  -> 클래스를 변경했을 때 변경된 클래스가 적용되게 하려면? <br>
  -> **User Defined Class Loader**가 필요하다.

<br>

### 메모리 (Memory)

**Method area (메소드 영역)**
> 클래스 수준의 정보(클래스 이름, 부모 클래스 이름, 메소드, 변수)를 저장하는 영역
- Class 영역, Static 영역이라고도 함
- Type 정보 (클래스, 인터페이스, Enum), 클래스 변수(static 변수), FQCN (Fully Qualified Class Name)을 저장
> FQCN (Fully Qualified Class Name) : 클래스가 속한 패키지명을 모두 포함한 이름
    ex) java.lang.String

**Stack area (스택 영역)**
> 메소드 내에서 정의하는 기본 자료형에 해당되는 지역변수(매개 변수 포함)의 데이터의 값이 저장되는 영역
- 메소드가 호출될 때 메모리에 할당되고 종료되면 메모리가 해제

**Heap area (힙 영역)**
> 인스턴스를 저장 및 공유하는 영역
- new 키워드로 생성된 객체와 배열이 생성되는 영역

**PC(Program Counter) Register (PC 레지스터)**
> Thread가 생성될 때 마다 생기는 영역
- 으로 Thread가 어떠한 명령을 실행하게 될지에 대한 부분을 기록.
- JVM은 *CPU에 직접 Instruction을 수행하지 않고 Stack에서 Operand를 뽑아내어 이를 별도의 메모리 공간(PC Registers)에 저장*하는 방식

**Native Method Stack (네이티브 메소드 스택)**
> 네이티브 메소드를 호출하는 코드를 수행하기 위한 스택
- 네이티브 메소드 (Native Method) : C, C++로 구현되어있는 메소드
- JNI(Java Native Interface)를 통해 Native Method Library를 사용

**JNI(Java Native Interface)**
> Java 어플리케이션에서 C, C++ 등 언어로 작성된 함수를 사용할 수 있는 인터페이스
- Native 키워드를 사용해 메소드를 호출
```java
   public static native Thread currentThread();
```
<br>

### Execution Engine (실행 엔진)

#### Interpreter (인터프리터)
> Bytecode를 기계가 이해할 수 있도록 Native Code로 변환<br>
> Native Code : OS에 의해 직접적으로 컴파일 되는 코드

- Bytecode 한 줄마다 컴파일을 하여 Native로 변환
- 중복되는 ByteCode들에 대해서도 매번 컴파일을 하게 되면 비효율적이며 Running Time도 길어짐
- 이러한 **중복되는 Byte Code에 대해서는 JIT 컴파일러를 사용**


#### JIT(Just In time) Compiler (JIT 컴파일러)
> 반복되는 코드를 모두 Native Code로 변환하는 컴파일러

- 반복된 Byte Code는 Native Code로 바뀌어 있기 때문에 Interpreter가 바로 사용할 수 있게 됨
- 컴파일 임계치가 일정 횟수에 도달한 코드는 바이트 코드가 실행되는 과정에서 기계어로 변환
> 컴파일 임계치 : **method entry counter**(JVM 내에 있는 메소드가 호출된 횟수) + **back-edge loop counter**(메소드가 루프를 빠져나오기까지 회전한 횟수)

#### Garbage Collection (가비지 컬렉션)
> 동적으로 할당했던 메모리 영역 중 필요 없게 된 메모리 영역을 주기적으로 삭제하는 프로세스

- Heap 영역의 더 이상 참조되지 않는 객체를 정리

<br>

> **참고**<br>
> [JVM 구조](https://goodgid.github.io/Java-JVM/#%EB%A9%94%EC%84%9C%EB%93%9C-%EC%98%81%EC%97%AD)<br>
> [[JAVA]자바의 기본 개념 정리-2.자바 메모리 구조](https://doohong.github.io/2018/03/02/Java-runtime-data-area/)<br>
> [JVM - 실행 엔진(Execution Engine)](https://junhyunny.github.io/information/java/jvm-execution-engine/)<br>
> [[Java] JVM 메모리 사용 영역](https://scshim.tistory.com/351)<br>
> [Java 프로그래밍 -메모리 구조-](https://yu5501.tistory.com/16)<br>
> [JVM 메모리 구조](https://velog.io/@kyukim/1-yylklo8g)<br>
