## 선택 정렬 (Selection Sort)

![](https://github.com/GimunLee/tech-refrigerator/raw/master/Algorithm/resources/selection-sort-001.gif)
```python
    """
        선택 정렬
        
        해당 순서에 원소를 넣을 위치는 이미 정해져 있고, 어떤 원소를 넣을지 선택하는 알고리즘
        
        첫 번째 순회에서 가장 최솟값을 찾아 넣는다.
        두 번째 순서에는 남은 값 중에서의 최솟값을 넣는다.
        ...
        하나의 원소만 남을 때까지 과정을 반복한다.
        
        시간복잡도는 최상 Ω(n^2), 평균 Θ(n^2), 최악 O(n^2)
        항상 이중루프 전부를 순회하기 때문
    """
    def selectionSort(arr):
        indexMin, temp = 0, 0
        for i in range(0, len(arr)-1):        
            indexMin = i
            for j in range(i + 1, len(arr)):  
                if arr[j] < arr[indexMin]:           
                    indexMin = j
            temp = arr[indexMin]
            arr[indexMin] = arr[i]
            arr[i] = temp
```
