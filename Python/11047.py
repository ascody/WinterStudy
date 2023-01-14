n, k = map(int, input().split())
arr = []

for i in range(n):
    arr.append(int(input()))
arr.reverse()

cnt = 0

while k > 0:
    for i in arr:
        if k - i >= 0:
            cnt += (k // i)
            k -= (i * (k // i))
print(cnt)