## 삽입 정렬 (Insertion Sort)

![](https://github.com/GimunLee/tech-refrigerator/raw/master/Algorithm/resources/insertion-sort-001.gif)
```python
    """
        삽입정렬
        
        2번째 원소부터 시작하여 그 앞(왼쪽)의 원소들과 비교하여 삽입할 위치를 지정한 후,
        원소를 뒤로 옮기고 지정된 자리에 자료를 삽입 하여 정렬하는 알고리즘
        
        2번째 원소부터 임시값에 저장한 후 앞의 원소들과 차례로 비교해나간다.
        앞 원소와 비교하여 앞 원소보다 더 작을 경우 앞 원소를 한칸 뒤로 이동시킨다.
        
        앞 원소보다 크면 그 자리에 삽입한다.
        
        시간복잡도는 평균 Θ(n^2), 최악 O(n^2)
        최선의 경우 Ω((n)
        모두 정렬되어 있을 경우 순회 한 번당 비교를 한 번씩만 하기 때문
    """
    def insertionSort(arr):
        for index in range(1, len(arr)):
            temp = arr[index]
            prev = index - 1
            while (prev >= 0) and (arr[prev] > temp):
                arr[prev+1] = arr[prev]
                prev -= 1
            arr[prev + 1] = temp
```
