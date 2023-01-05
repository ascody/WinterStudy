```python
# 1172 세 수 정렬하기
a = sorted(list(map(int, input().split())))
for i in a:
    print(i, end=' ')
```
```python
# 1420 3등 찾기
# 리스트에 딕셔너리를 넣어 점수를 기준으로 정렬
# 내림차순으로 정렬하여 2번 인덱스의 이름을 출력
n = int(input())
lst = []
for i in range(n):
    name, score = input().split()
    lst.append({'name':name, 'score':int(score)})
lst.sort(key=lambda x : x['score'], reverse=True)
print(lst[2]['name'])
```
```python
# 1441 버블 정렬
# 알고리즘은 맞으나 파이썬이 느려서 시간초과로 sort() 함수로 풀어야함
n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))
for i in range(n):
    for j in range(1, n-i):
        if(lst[j-1] > lst[j]):
            temp = lst[j]
            lst[j] = lst[j-1]
            lst[j-1] = temp
for i in lst:
    print(i)
```
```python
# 1442 선택 정렬
# 알고리즘은 맞으나 파이썬이 느려서 시간초과로 sort() 함수로 풀어야함
n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))
for i in range(n-1):
    min = i
    for j in range(i+1, n):
        if(lst[j] < lst[min]):
            min = j
    temp = lst[i]
    lst[i] = lst[min]
    lst[min] = temp
for i in lst:
    print(i)
```
```python
# 1443 삽입 정렬
# 알고리즘은 맞으나 파이썬이 느려서 시간초과로 sort() 함수로 풀어야함
n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))
for i in range(1, n):
    temp = lst[i]
    prev = i - 1
    while(prev >= 0 and temp < lst[prev]):
        lst[prev+1] = lst[prev]
        prev -= 1
    lst[prev+1] = temp
for i in lst:
    print(i)
```
```python
# 1451 데이터 정렬 (small)
n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))
for i in sorted(lst):
    print(i)
```
```python
# 1452 데이터 정렬 (large)
# 퀵 정렬 사용함
def quickSort(arr, first, last):
	if first >= last:
		return
	mid = partition(arr, first, last)
	quickSort(arr, first, mid-1)
	quickSort(arr, mid, last)
	return arr
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
n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))
quickSort(lst, 0, n-1)
for i in lst:
    print(i)
```
```python
# 1709 내림차순 정렬
n = int(input())
lst = list(map(int, input().split()))
for i in sorted(lst, reverse=True):
    print(i, end=' ')
```
```python
# 3004 데이터 재정렬
# 원 배열과 정렬 배열 2개를 만듦
# 원 배열을 순회하면서 각각의 인덱스값이 정렬 배열의 몇 번째에 있는지 확인한다.
# 정렬 배열을 검색하는 데 index() 함수를 사용하면 시간 초과가 나서 이분 탐색을 사용함
def search(arr, num):
    left = 0
    right = len(arr) - 1
    while(left <= right):
        mid = (left + right) // 2
        if(arr[mid] == num):
            return mid
        elif arr[mid] > num:
            right = mid -1
        else:
            left = mid + 1
n = int(input())
lst = list(map(int, input().split()))
slst = sorted(lst)
for i in lst:
    print(search(slst, i), end=' ')
```
```python
# 3011 거품 정렬(Bubble Sort)
# 순회가 한 번 실행된 후 앞뒤 값을 비교하여 정될되면 순회를 종료한다.
n = int(input())
lst = list(map(int, input().split()))
def count(n, lst):
    count = 0
    for i in range(n):
        count += 1
        for j in range(1, n-i):
            if(lst[j-1] > lst[j]):
                temp = lst[j]
                lst[j] = lst[j-1]
                lst[j-1] = temp
        check = True
        for i in range(n-1):
            if(lst[i] > lst[i+1]):
                check = False
                break
        if(check):
            return count
print(count(n, lst))
```