![](https://goodgid.github.io/assets/img/java/Java-JVM_1.png)

<h2>자바 컴파일과정</h2>

### 컴파일 (Compile)

개발자가 자바 소스코드를 작성

자바 컴파일러(Java Compiler)가 자바 소스파일을 컴파일

자바 소스코드(.java)가 자바 바이트 코드(.class)로 변환

자바 바이트 코드(Java bytecode)
: 자바 가상 머신이 이해할 수 있는 언어로 변환된 자바 소스코드

바이트 코드를 클래스로더에 전달

**자바 소스코드 (.java) -> 자바 바이트 코드 (.class)**

### 클래스 로더 (Class Loader)

동적로딩(Dynamic Loading)을 통해 **필요한 클래스**들을 로딩 및 링크

런타임 데이터 영역(Runtime Data area), 즉 **JVM의 메모리에 올림**

**런타임**(바이트 코드를 실행할 때)에 클래스를 로드하고 링크.

**로딩 -> 링크 -> 초기화**의 순서로 진행된다.

#### 로딩(loading)

.class 파일을 읽고 그 내용에 따라 적절한 **바이너리 데이터를 만들고 Method 영역에 저장**

Method 영역에 저장하는 데이터

  - **Type 정보**
  
  - **메소드와 클래스 변수**(=Static변수)
  
  - **Fully Qualified Class Name**(클래스가 속한 패키지명을 모두 포함한 이름)

로딩이 끝나면 해당 Class Type의 Class 객체를 생성하여 힙 영역(인스턴스를 저장 및 공유하는 영역)에 저장

클래스 로더의 종류는 Bootstrap, Extension, Application 3가지

Bootstrap -> Extension -> Application 순으로 구동

**Bootstrap ClassLoader**

최상위 클래스로더로, JVM 을 구동시키기 위한 가장 필수적인 라이브러리의 클래스들을 JVM 에 탑재

**Extension ClassLoader**

표준 핵심 Java Class 의 라이브러리들을 JVM 에 탑재

**Application ClassLoader**

개발자들이 자바 코드로 짠 클래스 파일들을 JVM 에 탑재

#### 링크(linking)

링크 작업은 **Verify -> Prepare -> Resolve** 3단계로 이뤄진다.

**Verify(검증)**
  class 파일 형식이 자바 언어 명세(Java Language Specification) 및 JVM 명세에 명시된 대로 구성되어 있는지 검사

**Prepare(준비)**
  클래스 변수(static 변수)와 기본값에 필요한 메모리를 할당 (필드, 메서드, 인터페이스 등등)

**Resolve(분석)**
  클래스의 상수 풀 내 모든 심볼릭 레퍼런스를 다이렉트 레퍼런스로 변경

참조변수를 heap에 저장된 인스턴스와 연결하는 과정
    
#### 초기화(initialization)

static으로 선언된 변수와 메소드에 메모리를 할당해 초기값을 채우는 과정

**클래스로더를 알아야하는 이유**

- was에 내가 만든 웹앱이 올라가는 경우

클래스로더에 메모리를 올리면 프로그램 종료 이외에는 클래스 정보를 지우는 방법이 따로 없음.

  -> 코드를 수정해서 재배포하기 어려움 
  -> 클래스를 변경했을 때 변경된 클래스가 적용되게 하려면? 
  -> User Defined Class Loader가 필요하다.
