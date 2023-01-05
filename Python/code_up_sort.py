# # 1172 세 수 정렬하기
# a = sorted(list(map(int, input().split())))
# for i in a:
#     print(i, end=' ')


# # 1420 3등 찾기
# n = int(input())
# lst = []
# for i in range(n):
#     name, score = input().split()
#     lst.append({'name':name, 'score':int(score)})
# lst.sort(key=lambda x : x['score'], reverse=True)
# print(lst[2]['name'])

# # 1441 버블 정렬
# n = int(input())
# lst = []
# for i in range(n):
#     lst.append(int(input()))
# for i in range(n):
#     for j in range(1, n-i):
#         if(lst[j-1] > lst[j]):
#             temp = lst[j]
#             lst[j] = lst[j-1]
#             lst[j-1] = temp
# for i in lst:
#     print(i)


# # 1442 선택 정렬
# n = int(input())
# lst = []
# for i in range(n):
#     lst.append(int(input()))
# for i in range(n-1):
#     min = i
#     for j in range(i+1, n):
#         if(lst[j] < lst[min]):
#             min = j
#     temp = lst[i]
#     lst[i] = lst[min]
#     lst[min] = temp
# for i in lst:
#     print(i)


# # 1443 삽입 정렬
# n = int(input())
# lst = []
# for i in range(n):
#     lst.append(int(input()))
# for i in range(1, n):
#     temp = lst[i]
#     prev = i - 1
#     while(prev >= 0 and temp < lst[prev]):
#         lst[prev+1] = lst[prev]
#         prev -= 1
#     lst[prev+1] = temp
# for i in lst:
#     print(i)


# # 1451 데이터 정렬 (small)
# n = int(input())
# lst = []
# for i in range(n):
#     lst.append(int(input()))
# for i in sorted(lst):
#     print(i)


# # 1452 데이터 정렬 (large)
# def quickSort(arr, first, last):
# 	if first >= last:
# 		return
# 	mid = partition(arr, first, last)
# 	quickSort(arr, first, mid-1)
# 	quickSort(arr, mid, last)
# 	return arr
# def partition(arr, first, last):
# 	pivot = arr[(first + last) // 2]
# 	while first <= last:
# 		while arr[first] < pivot:
# 			first += 1
# 		while arr[last] > pivot:
# 			last -= 1
# 		if first <= last:
# 			arr[first], arr[last] = arr[last], arr[first]
# 			first, last = first + 1, last - 1
# 	return first
# n = int(input())
# lst = []
# for i in range(n):
#     lst.append(int(input()))
# quickSort(lst, 0, n-1)
# for i in lst:
#     print(i)

# # 1709 내림차순 정렬
# n = int(input())
# lst = list(map(int, input().split()))
# for i in sorted(lst, reverse=True):
#     print(i, end=' ')

# # 3004 데이터 재정렬
# def search(arr, num):
#     left = 0
#     right = len(arr) - 1
#     while(left <= right):
#         mid = (left + right) // 2
        
#         if(arr[mid] == num):
#             return mid
#         elif arr[mid] > num:
#             right = mid -1
#         else:
#             left = mid + 1
    
# n = int(input())
# lst = list(map(int, input().split()))
# slst = sorted(lst)
# for i in lst:
#     print(search(slst, i), end=' ')

# # 3011 거품 정렬(Bubble Sort)
# n = int(input())
# lst = list(map(int, input().split()))
# def count(n, lst):
#     count = 0
#     for i in range(n):
#         count += 1
#         for j in range(1, n-i):
#             if(lst[j-1] > lst[j]):
#                 temp = lst[j]
#                 lst[j] = lst[j-1]
#                 lst[j-1] = temp
#         check = True
#         for i in range(n-1):
#             if(lst[i] > lst[i+1]):
#                 check = False
#                 break
#         if(check):
#             return count
# print(count(n, lst))


# # 3014 정렬을 빠르게!
# n = int(input())
# lst = list(map(int, input().split()))
# cnt = [0] * (max(lst) + 1)
# ans = [0] * (n + 1)
# for i in lst:
#     cnt[i] += 1
# for i in range(1, len(cnt)):
#     cnt[i] += cnt[i-1]
# for i in lst:
#     ans[cnt[i]-1] = i
#     cnt[i] -= 1
# for i in range(n):
#     print(ans[i], end=' ')


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