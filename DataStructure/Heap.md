## Heap

### 힙 (Heap)
> 완전 이진 트리의 일종으로 우선순위 큐를 위하여 만들어진 자료구조

- **최댓값이나 최솟값을 빠르게** 찾아내도록 만들어진 자료구조

- 반정렬 상태를 유지

- 중복된 값을 허용

#### 우선순위 큐 (Priority Queue)
> 먼저 들어오는 데이터가 아니라, 우선순위가 높은 데이터가 먼저 나가는 형태의 자료구조

![](https://gmlwjd9405.github.io/images/data-structure-heap/types-of-heap.png)

#### 최대 힙 (Max Heap)
> 부모 노드의 키값이 자식 노드의 키값보다 항상 큰 힙

#### 최소 힙 (Min Heap)
>  부모 노드의 키값이 자식 노드의 키값보다 항상 작은 힙

### 시간 복잡도
![](https://velog.velcdn.com/images%2Fyanghl98%2Fpost%2Fc64db4c9-6151-4c26-9f06-bb2b9193168a%2Fimage.png)

### 노드 관계

#### 0-base (0번 인덱스부터)
- 왼쪽 자식 : (부모 index) x 2 + 1
- 오른쪽 자식 : (부모 index) x 2 + 2
- 부모 : (자식 index) / 2 - 1

#### 1-base (1번 인덱스부터)
- 왼쪽 자식 : (부모 index) x 2
- 오른쪽 자식 : (부모 index) x 2 + 1
- 부모 : (자식 index) / 2

### 힙의 구현

#### 삽입
![](https://velog.velcdn.com/images%2Femplam27%2Fpost%2F5afbb3d1-83b3-4fdb-98c9-5969296f43f0%2F%ED%9E%99%20-%20%EB%85%B8%EB%93%9C%20%EC%82%BD%EC%9E%85.png)

```python
def up_heapify(index, heap):
    child_index = index
    while child_index != 0:
        parent_index = (child_index - 1) // 2
        if heap[parent_index] < heap[child_index]:
            heap[parent_index], heap[child_index] = heap[child_index], heap[parent_index]
            child_index = parent_index
        else:
            return
```

#### 삭제
![](https://velog.velcdn.com/images%2Femplam27%2Fpost%2Fd9151cfd-aec6-4f48-87ce-30eef782feb1%2F%ED%9E%99%20-%20%ED%9E%99%20%EC%9E%AC%EA%B5%AC%EC%A1%B0.png)

```python
def find_bigger_child_index(index, heap_size):
    parent = index
    left_child = (parent * 2) + 1
    right_child = (parent * 2) + 2

    if left_child < heap_size and heap[parent] < heap[left_child]:
        parent = left_child
    if right_child < heap_size and heap[parent] < heap[right_child]:
        parent = right_child
    return parent


def down_heapify(index, heap):
    parent_index = index
    bigger_child_index = find_bigger_child_index(parent_index, len(heap))
    while parent_index != bigger_child_index:
        heap[parent_index], heap[bigger_child_index] = heap[bigger_child_index], heap[parent_index]
        parent_index = bigger_child_index
        bigger_child_index = find_bigger_child_index(parent_index, len(heap))
```


#### build heap
> 힙이 아닌 배열을 힙으로 만들기

![](https://velog.velcdn.com/images%2Femplam27%2Fpost%2Fb7a8132a-ec63-447d-9b98-a880b06938cf%2F%ED%9E%99%20-%20%EB%B0%B0%EC%97%B4%EC%9D%84%20%ED%9E%99%EC%9C%BC%EB%A1%9C.png)

```python
 def make_heap(array, index, heap_size):
        parent = index
        left_child = 2 * parent + 1
        right_child = 2 * parent + 2

        if left_child < heap_size and array[left_child] > array[parent]:
            parent = left_child
        if right_child < heap_size and array[right_child] > array[parent]:
            parent = right_child
        if parent != index:
            array[parent], array[index] = array[index], array[parent]
            make_heap(array, parent, heap_size)
	
    # 부모노드가 되는 노드들만을 골라서 뒤에서부터 heapify를 차례로 실행
    for i in range((N - 1) // 2, -1, -1):
        make_heap(array, i, heap_size)
```

> **참조**   
> [[자료구조] 힙(Heap)](https://github.com/gyoogle/tech-interview-for-developer/blob/master/Computer%20Science/Data%20Structure/Heap.md)   
> [[자료구조] 힙(heap)이란](https://gmlwjd9405.github.io/2018/05/10/data-structure-heap.html)   
> [[자료구조] 힙 트리(Heap Tree)](https://velog.io/@redgem92/%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-%ED%9E%99-%ED%8A%B8%EB%A6%ACHeap-Tree)   
> [[자료구조] Heap(힙) - 개념, 종류, 활용 예시, 구현](https://velog.io/@yanghl98/%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-Heap%ED%9E%99-%EA%B0%9C%EB%85%90-%EC%A2%85%EB%A5%98-%ED%99%9C%EC%9A%A9-%EC%98%88%EC%8B%9C-%EA%B5%AC%ED%98%84)   
> [[자료구조] 그림으로 알아보는 힙(Heap)](https://velog.io/@emplam27/%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-%EA%B7%B8%EB%A6%BC%EC%9C%BC%EB%A1%9C-%EC%95%8C%EC%95%84%EB%B3%B4%EB%8A%94-%ED%9E%99Heap)   
