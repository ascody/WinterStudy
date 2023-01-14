# 30 = 3 X 10
# 3의 배수 : 각 자리 수의 합이 3의 배수
# 10의 배수 : 일의 자리가 0
n = input()

if("0" not in n or int(n) < 30):
    print('-1')
else:
    n = list(n)
    if(sum(list(map(int, n))) % 3 == 0):
        n.sort(reverse=True)
        print(int(''.join((n))))
    else:
        print("-1")