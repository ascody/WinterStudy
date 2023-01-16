## 큐 (Queue)

![](https://velog.velcdn.com/images%2Fawesomeo184%2Fpost%2Fc1d73c47-1103-4c47-94cd-8563e85b6542%2F%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202020-10-07%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%2010.25.31.png)

> <b>FIFO (First In First Out, 선입선출) 방식의 자료구조</b>

```Python
    import queue

    lst = queue.Queue()

    lst.put(1)
    lst.put(2)
    lst.put(3) # [1, 2, 3]

    print("size:", lst.qsize())
    print("dequeue:", lst.get()) # [2, 3]
```
