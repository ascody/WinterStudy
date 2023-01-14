n, m = map(int, input().split())
cnt = 0

# 나이트가 모든 방법을 사용할 수 있는 최소 크기 3 X 6

if n == 1:
    cnt = 1
elif n == 2:
    cnt = 4 if (m-1) // 2 + 1 > 4 else (m-1) // 2 + 1
else:
    if m <= 6:
        cnt = 4 if m > 4 else m
    else:
        cnt = m - 2

print(cnt)