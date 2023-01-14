num = int(input())

arr = []
for i in range(num):
    arr.append(list(map(int, input().split())))
arr.sort(key = lambda x:(x[1], x[0]))

cnt = 1
former = arr[0]
for i in range(1, len(arr)):
    if former[1] <= arr[i][0]:
        cnt += 1
        former = arr[i]
if former[1] < arr[0][0]:
    cnt -= 1
print(cnt)