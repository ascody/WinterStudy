# n = 여학생의 수
# m = 남학생의 수
# k = 인턴쉽에 참여해야 하는 인원

n, m, k = map(int, input().split())

for i in range(k):
    if(n // 2 >= m):
        n -= 1
    else:
        m -= 1
num = n // 2 if n // 2 < m else m
print(num)