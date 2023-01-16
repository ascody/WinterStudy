## 스택 (Stack)

![](https://images.velog.io/images/awesomeo184/post/c6d03dfa-ca41-46ef-b3bd-3524c7c704c4/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202020-10-07%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%208.25.11.png)

> <b>LIFO (Last In First Out, 후입선출) 방식의 자료구조</b>

```Python
    a_list = [1,2,3]

    # 데이터를 추가
    a_list.append(1) # [1, 2, 3, 1]
    a_list.pop() # [1, 2, 3]

    a_list = [1,2,3]
    a_list.pop() # [1, 2]

    # 파이썬의 pop()은 삭제한 요소를 반환함
    print(a_list.pop())
```
