## 퀵 정렬 (Quick Sort)

![](https://velog.velcdn.com/images/aiden/post/e7751711-c825-4b1c-b625-67c87a93583c/%ED%80%B5%20%EC%A0%95%EB%A0%AC.gif)
> 참고자료 : [https://st-lab.tistory.com/250](https://st-lab.tistory.com/250)
```python
    """
        퀵 정렬
        
        분할정복(Divide and Conquer)을 이용하는 정렬 알고리즘
        
        리스트 안에 있는 한 요소를 선택한다. 이를 pivot이라고 한다.
        
        pivot보다 작은 요소들은 모두 pivot의 왼쪽으로 옮기고
        pivot보다 큰 요소들은 모두 pivot의 오른쪽으로 옮긴다.
        
        pivot을 제외한 왼쪽 리스트와 오른쪽 리스트를 다시 정렬한다.
        분할된 왼쪽 리스트와 오른쪽 리스트도 다시 pivot을 정하고 pivot을 기준으로 2개의 부분리스트로 나눈다.
        재귀를 사용하여 부분 리스트들이 더이상 분할이 불가능 할 때까지 반복한다. 
        
        최악의 경우 O(n^2), 평균적으로 Θ(nlogn)의 복잡도를 가짐
        최악의 경우는 피벗값이 최댓값이거나 최솟값일 때인데, 베열이 이미 정렬되어있는 경우 최악의 시간복잡도를 가진다.
        부분 배열이 한개씩 분할되어 순환 호출의 깊이가 n이 된다.
        
        이를 해결하기 위해 pivot값을 중간값으로 결정한다.
        부분 배열이 한개씩 분할되는 경우를 방지한다.
        
        아래 코드는 이를 해결한 코드다.
    """
    # 부분 배열을 정렬하는 함수
    def quickSort(arr, first, last):
        if first >= last:
            return
        mid = partition(arr, first, last)
        quickSort(arr, first, mid-1)
        quickSort(arr, mid, last)
        return arr
    # 피벗을 기준으로 비균등하게 2개의 부분 배열로 분할하는 함수
    def partition(arr, first, last):
        pivot = arr[(first + last) // 2]
        while first <= last:
            while arr[first] < pivot:
                first += 1
            while arr[last] > pivot:
                last -= 1
            if first <= last:
                arr[first], arr[last] = arr[last], arr[first]
                first, last = first + 1, last - 1
        return first
```
