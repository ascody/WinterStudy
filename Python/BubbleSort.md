> <b>버블정렬 (Bubble Sort)</b>

![](https://github.com/GimunLee/tech-refrigerator/raw/master/Algorithm/resources/bubble-sort-001.gif)
```python
    """
        버블정렬
        
        서로 인접한 두 원소를 검사하여 정렬하는 알고리즘
        크기가 순서대로 되어있지 않으면 서로 교환한다.
        순회가 한 번 끝날 때마다 끝에서부터 차례로 정렬된다.
        원소의 이동이 거품이 수면으로 올라오는 듯한 모습을 보이기 때문에 이런 이름이 지어짐
        
        첫 순회는 arr[0] <-> arr[1], arr[1] <-> arr[2], ..., arr[n-1] <-> arr[n]
        두 번째 순회는 arr[0] <-> arr[1], arr[1] <-> arr[2], ..., arr[n-2] <-> arr[n-1]
        ...
        마지막 순회는 arr[0] <-> arr[1]
        
        시간복잡도는 최상 Ω(n^2), 평균 Θ(n^2), 최악 O(n^2)
        항상 이중루프 전부를 순회하기 때문
    """
    def bubbleSort(arr):
        temp = 0
        for i in range(0, len(arr)):
            for j in range(1, len(arr)-i):
                if arr[j-1] > arr[j]:
                    temp = arr[j-1]
                    arr[j-1] = arr[j]
                    arr[j] = temp
```
