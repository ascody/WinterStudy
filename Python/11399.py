num = int(input())
arr = list(map(int, input().split()))
arr.sort()

for i in range(1, len(arr)):
    arr[i] += arr[i-1]

print(sum(arr))