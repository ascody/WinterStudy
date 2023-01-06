<h2>Call by Value와 Call by Reference</h2>

> 참고 : [https://stackoverflow.com/questions/40480/is-java-pass-by-reference-or-pass-by-value](https://stackoverflow.com/questions/40480/is-java-pass-by-reference-or-pass-by-value)

### call by value
> <b>값에 의한 호출</b>

- 함수가 호출될 때, 메모리 공간 안에서는 함수를 위한 별도의 임시공간이 생성됨 (종료 시 해당 공간 사라짐)

- call by value 호출 방식은 함수 호출 시 전달되는 변수 값을 복사해서 함수 인자로 전달함

- 이때 복사된 인자는 함수 안에서 지역적으로 사용되기 때문에 local value 속성을 가짐

### call by reference
> **참조에 의한 호출**

- call by reference 호출 방식은 함수 호출 시 인자로 전달되는 변수의 레퍼런스를 전달함

- 따라서 함수 안에서 인자 값이 변경되면, 아규먼트로 전달된 객체의 값도 변경됨

### Java 함수 호출 방식

**객체 Integer를 swap하려 했으나 바뀌지 않는다.**
```Java
public class Test {
    private static void swap(Integer a, Integer b) {
        Integer temp = a;
        a = b;
        b = temp;
    }
    public static void main(String args[]) {
        Integer a = new Integer(1);
        Integer b = new Integer(2);

        System.out.println("a => " + a.intValue());
        System.out.println("b => " + b.intValue());

        swap(a, b);

        System.out.println("------- swap 후 -------");

        System.out.println("a => " + a.intValue());
        System.out.println("b => " + b.intValue());
    }
}
```

- 자바는 무조건 Call by Value 방식으로 전달한다.

- 참조변수의 경우 참조를 전달할 것이라 생각할 수 있으나 그렇지 않다.

- 자바는 참조가 아닌 객체의 주소값을 복사하여 전달한다.

#### 다른 언어가 객체를 전달하는 경우

- 참조를 전달한다.

- caller와 callee 같은 값을 공유한다.

#### 자바가 객체를 전달하는 경우

- 주소의 복사본을 전달한다.

- 프로퍼티에는 접근할 수 있으나 객체 자체를 변경하지는 못한다.

#### 비유

- 연필 객체가 있다고 하자.

- Call by Reference는 연필의  전달한다. (연필 자체를 공유)

- 자바는 연필이 있는 주소를 전달한다. (연필 주소를 공유)
