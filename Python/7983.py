num = int(input())
arr = [list(map(int, input().split())) for _ in range(num)]

arr.sort(reverse=True, key=lambda x:x[1])
max = arr[0][1]

for i in range(num):
    max = min(arr[i][1], max) - arr[i][0]
print(max)