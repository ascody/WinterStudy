### 코드업 파이썬 기초 100제

```python
    # 6001 출력하기01
    print("Hello")
```
```python
    # 6002 출력하기02
    print("Hello World")
```
```python
    # 6003 출력하기03
    print("Hello")
    print("World")
```
```python
    # 6004 출력하기04
    print("'Hello'")
```
```python
    # 6005 출력하기05
    print('"Hello World"')
```
```python
    # 6006 출력하기06
    print("\"!@#$%^&*()'")
```
```python
    # 6007 출력하기07
    print("\"C:\\Download\\'hello'.py\"")
```
```python
    # 6008 출력하기08
    print('print("Hello\\nWorld")')
```
```python
    # 6009 문자 1개 입력받아 그대로 출력하기
    print(input())
```
```python
    # 6010 정수 1개 입력받아 int로 변환하여 출력하기
    print(int(input()))
```
```python
    # 6011 실수 1개 입력받아 변환하여 출력하기
    print(float(input()))
```
```python
    # 6012 정수 2개 입력받아 그대로 출력하기1
    print(int(input()), "\n", int(input()), sep='')
```
```python
    # 6013 문자 2개 입력받아 순서 바꿔 출력하기1
    a, b = input(), input()
    print(b + "\n" + a)
```
```python
    # 6014 실수 1개 입력받아 3번 출력하기
    a = float(input())
    print(a,'\n',a,'\n',a, sep='')
```
```python
    # 6015 정수 2개 입력받아 그대로 출력하기2
    a, b = map(int, input().split())
    print(a, "\n", b, sep='')
```
```python
    # 6016 문자 2개 입력받아 순서 바꿔 출력하기2
    b, a = input().split()
    print(a, "\n", b, sep='')
```
```python
    # 6017 문장 1개 입력받아 3번 출력하기
    a = input()
    print(a, a, a)
```
```python
    # 6018 시간 입력받아 그대로 출력하기
    a, b = input().split(':')
    print(a, b, sep=':')
```
```python
    # 6019 연월일 입력받아 순서 바꿔 출력하기
    y, m, d = input().split('.')
    print(d, m, y, sep='-')
```
```python
    # 6020 주민번호 입력받아 형태 바꿔 출력하기
    a = input().replace('-','')
    print(a)
```
```python
    # 6021 단어 1개 입력받아 나누어 출력하기
    s = input()
    for i in s:
        print(i)
```
```python
    # 6022 연월일 입력받아 나누어 출력하기
    s = input()
    print(s[0:2], s[2:4], s[4:])
```
```python
    # 6023 시분초 입력받아 분만 출력하기
    h, m, s = input().split(':')
    print(m)
```
```python
    # 6024 단어 2개 입력받아 이어 붙이기
    w1, w2 = input().split()
    print(w1 + w2)
```
```python
    # 6025 정수 2개 입력받아 합 계산하기
    a, b = input().split()
    print(int(a) + int(b))
```
```python
    # 6026 실수 2개 입력받아 합 계산하기
    a, b = float(input()),float(input())
    print(a + b)
```
```python
    # 6027 10진 정수 입력받아 16진수로 출력하기1
    a = int(input())
    print('%x'% a)
```
```python
    # 6028 10진 정수 입력받아 16진수로 출력하기2
    a = int(input())
    print('%X'% a)
```
```python
    # 6029 16진 정수 입력받아 8진수로 출력하기
    a = int(input(), 16)
    print('%o'% a)
```
```python
    # 6030 영문자 1개 입력받아 10진수로 변환하기
    print(ord(input()))
```
```python
    # 6031 정수 입력받아 유니코드 문자로 변환하기
    print(chr(int(input())))
```
```python
    # 6032 정수 1개 입력받아 부호 바꾸기
    print(-int(input()))
``` 
```python
    # 6033 문자 1개 입력받아 다음 문자 출력하기
    print(chr(ord(input())+1))
```
```python
    # 6034 정수 2개 입력받아 차 계산하기
    a, b = input().split()
    print(int(a) - int(b))
```
```python
    # 6035 실수 2개 입력받아 곱 계산하기
    a, b = input().split()
    print(float(a) * float(b))
```
```python
    # 6036 단어 여러 번 출력하기
    w, n = input().split()
    print(w*int(n))
```
```python
    # 6037 문장 여러 번 출력하기
    n, s = input(), input()
    print(int(n)*s)
```
```python
    # 6038 정수 2개 입력받아 거듭제곱 계산하기
    a, b = input().split()
    print(int(a) ** int(b))
```
```python
    # 6039 실수 2개 입력받아 거듭제곱 계산하기
    a, b = input().split()
    print(float(a) ** float(b))
```
```python
    # 6040 정수 2개 입력받아 나눈 몫 계산하기
    a, b = input().split()
    print(int(a) // int(b))
```
```python
    # 6041 정수 2개 입력받아 나눈 나머지 계산하기
    a, b = input().split()
    print(int(a) % int(b))
```
```python
    # 6042 실수 1개 입력받아 소숫점이하 자리 변환하기
    print( format(float(input()), ".2f") )
```
```python
    # 6043 실수 2개 입력받아 나눈 결과 계산하기
    a, b = input().split()
    print("{:.3f}".format(float(a) / float(b)))
    # print(f'{float(a) / float(b):.3f}')
```
```python
    # 6044 정수 2개 입력받아 자동 계산하기
    a, b = map(int, input().split())
    print(a + b, a - b, a * b, a // b, a % b, f'{a / b:.2f}', sep='\n', end='')
```
```python
    # 6045 정수 3개 입력받아 합과 평균 출력하기
    a, b, c = map(int, input().split())
    print(a+b+c, f'{(a+b+c)/3.0:.2f}')
```
```python
    # 6046 정수 1개 입력받아 2배 곱해 출력하기
    print(int(input()) << 1)
```
```python
    # 6047 2의 거듭제곱 배로 곱해 출력하기
    a, b = map(int, input().split())
    print(a << b)
```
```python
    # 6048 정수 2개 입력받아 비교하기1
    a, b = map(int, input().split())
    print(a < b)
```
```python
    # 6049 정수 2개 입력받아 비교하기2
    a, b = map(int, input().split())
    print(a == b)
```
```python
    # 6050 정수 2개 입력받아 비교하기3
    a, b = map(int, input().split())
    print(a <= b)
```
```python
    # 6051 정수 2개 입력받아 비교하기4
    a, b = map(int, input().split())
    print(a != b)
```
```python
    # 6052 정수 입력받아 참 거짓 평가하기
    print(bool(int(input())))
```
```python
    # 6053 참 거짓 바꾸기
    print(not bool(int(input())))
```
```python
    # 6054 둘 다 참일 경우만 참 출력하기
    a, b = input().split()
    print(bool(int(a)) and bool(int(b)))
```
```python
    # 6055 하나라도 참이면 참 출력하기
    a, b = input().split()
    print(bool(int(a)) or bool(int(b)))
```
```python
    # 6056 참/거짓이 서로 다를 때에만 참 출력하기
    a, b = map(bool, map(int, input().split()))
    print((a and (not b)) or ((not a) and b))
```
```python
    # 6057 참/거짓이 서로 같을 때에만 참 출력하기
    a, b = map(bool, map(int, input().split()))
    print((not (a) and (not b)) or (a and b))
```
```python
    # 6058 둘 다 거짓일 경우만 참 출력하기
    a, b = map(bool, map(int, input().split()))
    print(not (a or b))
```
```python
    # 6059 비트단위로 NOT 하여 출력하기
    print(~int(input()))
```
```python
    # 6060 비트단위로 AND 하여 출력하기
    a, b = map(int, input().split())
    print(a & b)
```
```python
    # 6061 비트단위로 OR 하여 출력하기
    a, b = map(int, input().split())
    print(a | b)
```
```python
    # 6062 비트단위로 XOR 하여 출력하기
    a, b = map(int, input().split())
    print(a ^ b)
```
```python
    # 6063 정수 2개 입력받아 큰 값 출력하기
    a, b = map(int, input().split())
    print(a if a >= b else b)
```
```python
    # 6064 정수 3개 입력받아 가장 작은 값 출력하기
    a, b, c = map(int, input().split())
    print((a if a <= b else b) if b <= c else c)
```
```python
    # 6065 정수 3개 입력받아 짝수만 출력하기
    s = [i for i in map(int,input().split()) if i % 2 == 0]
    for i in s: 
        print(i)
```
```python
    # 6066 정수 3개 입력받아 짝/홀 출력하기
    s = map(int,input().split())
    s = ['even' if i % 2 == 0 else 'odd' for i in s] 
    for i in s: 
        print(i)
```
```python
    # 6067 정수 1개 입력받아 분류하기
    a = int(input())
    print(('A' if a % 2 == 0 else 'B') if a < 0 else ('C' if a % 2 == 0 else 'D'))
```
```python
    # 6068 점수 입력받아 평가 출력하기
    a = int(input())
    print(('A' if a >= 90 else 'B') if a >= 70 else ('C' if a >= 40 else 'D'))
```
```python
    # 6069 평가 입력받아 다르게 출력하기
    a = input()
    print("best!!!" if a == 'A' else ('good!!' if a == 'B' else ('run!' if a == 'C' else ('slowly~' if a == 'D' else 'what?'))))

    # 6070 월 입력받아 계절 출력하기
    a = int(input())
    print("winter" if a % 12 <= 2 else ('spring' if a % 12 <= 5 else ('summer' if a % 12 <= 8 else 'fall')))
```
```python
    # 6071 0 입력될 때까지 무한 출력하기
    n = 1
    while n != 0:
        n = int(input())
        if(n != 0):
            print(n)
```
```python
    # 6072 정수 1개 입력받아 카운트다운 출력하기1
    n = int(input())
    while n!=0 :
    print(n)
    n = n-1
```
```python
    # 6073 정수 1개 입력받아 카운트다운 출력하기2
    n = int(input())
    while n!=0 :
    n = n-1
    print(n)
```
```python
    # 6074 문자 1개 입력받아 알파벳 출력하기
    c = ord(input())
    t = ord('a')
    while t<=c :
    print(chr(t), end=' ')
    t += 1
```
```python
    # 6075 정수 1개 입력받아 그 수까지 출력하기
    n = int(input())
    i = 0
    while i <= n :
    print(i)
    i = i+1
```
```python
    # 6076 정수 1개 입력받아 그 수까지 출력하기2
    n = int(input())
    for i in range(n+1):
    print(i)
```
```python
    # 6077 짝수 합 구하기
    n = sum([i for i in list(range(1, int(input())+1)) if i % 2 == 0])
    print(n)
```
```python
    # 6078 원하는 문자가 입력될 때까지 반복 출력하기
    n = ''
    while n != 'q':
        n = input()
        print(n)
```
```python
    # 6079 언제까지 더해야 할까?
    n = int(input())
    i = 1
    sum = 1
    while (sum < n):
        i += 1
        sum += i
    print(i)
```
```python
    # 6080 주사위 2개 던지기
    n, m = map(int, input().split())
    for i in range(1, n+1) :
    for j in range(1, m+1) :
        print(i, j)
```
```python
    # 6081 16진수 구구단 출력하기
    n = int(input(), 16)
    for i in range(1, 0xf+1):
        print('%X'%n,'*','%X'%i,'=','%X'%(n*i), sep='')
```
```python
    # 6082 3 6 9 게임의 왕이 되자
    for i in range(1, int(input())+1):
        if i % 10==3 or i % 10 == 6 or i % 10==9 or i // 10 == 3:
            print("X", end=' ')
        else:
            print(i, end=' ')
```
```python
    # 6083 빛 섞어 색 만들기
    a, b, c = map(int, input().split())
    count = 0
    for i in range(a):
        for j in range(b):
            for k in range(c):
                print(i, j, k)
                count += 1
    print(count)
```
```python
    # 6084 소리 파일 저장용량 계산하기
    h, b, c, s = map(int, input().split())
    print(f'{h*b*c*s/8/1024/1024:.1f} MB')
```
```python
    # 6085 그림 파일 저장용량 계산하기
    w, h, b = map(int, input().split())
    print(f'{w*h*b/8/1024/1024:.2f} MB')
```
```python
    # 6086 거기까지! 이제 그만~
    n = int(input())
    s = 0
    i = 1
    while True:
        s += i
        i += 1
        if s >= n:
            print(s)
            break
```
```python
    # 6087 3의 배수는 통과
    n = int(input())
    for i in range(1, n+1):
        if(i % 3 != 0):
            print(i, end=' ')
```
```python
    # 6088 수 나열하기1
    a, d, n = map(int, input().split())
    for i in range(n-1):
        a += d
    print(a)
```
```python
    # 6089 수 나열하기2
    a, r, n = map(int, input().split())
    for i in range(n-1):
        a *= r
    print(a)
```
```python
    # 6090 수 나열하기3
    a, m, d, n = map(int, input().split())
    for i in range(n-1):
        a = a * m + d
    print(a)
```
```python
    # 6091 함께 문제 푸는 날
    a, b, c = map(int, input().split())
    d = 1
    while d%a!=0 or d%b!=0 or d%c!=0 :
    d += 1
    print(d)
```
```python
    # 6092 이상한 출석 번호 부르기1
    n, c = int(input()), map(int,input().split())
    check = [0 for i in range(23)]
    for i in c:
        check[i-1] += 1
    for i in check:
        print(i, end=' ')
```
```python
    # 6093 이상한 출석 번호 부르기2
    n, c = int(input()), list(map(int,input().split()))
    for i in reversed(c):
        print(i, end=' ')
```
```python
    # 6094 이상한 출석 번호 부르기3
    n, c = int(input()), list(map(int,input().split()))
    print(sorted(c)[0])
```
```python
    # 6095 바둑판에 흰 돌 놓기
    n = int(input())
    a = [[0 for i in range(19)] for i in range(19)]
    for i in range(n):
        x, y = map(int, input().split())
        a[x-1][y-1] = 1
    for i in range(19):
        for j in range(19):
            print(a[i][j], end =' ')
        print('')
```
```python
    # 6096 바둑알 십자 뒤집기
    board = []
    for i in range(19):
        board.append(list(map(int, input().split())))
    n = int(input())    
    for i in range(n):
        x, y = map(int, input().split())
        for j in range(19):
            board[x-1][j] = int(not board[x-1][j])
        for j in range(19):
            board[j][y-1] = int(not board[j][y-1])
    for i in range(19):
        for j in range(19):
            print(board[i][j], end =' ')
        print('')
```
```python
    # 6097 설탕과자 뽑기
    h, w = map(int, input().split())
    board = [[0 for i in range(w)] for i in range(h)]
    n = int(input())
    for i in range(n):
        l, d, x, y = map(int, input().split())
        if(d == 0):
            for j in range(l):
                board[x-1][y-1+j] = 1   
        elif(d == 1):
            for j in range(l):
                board[x-1+j][y-1] = 1
    for i in range(h):
        for j in range(w):
            print(board[i][j], end =' ')
        print('')
```
```python
    # 6098 성실한 개미
    board = []
    for i in range(10):
        board.append(list(map(int, input().split())))
    x = 1
    y = 1
    check = True
    while check:
        if board[x][y] == 2:
            board[x][y] = 9
            check = False
        board[x][y] = 9
        if board[x][y+1] == 0 or board[x][y+1] == 2:
            y += 1
        elif board[x+1][y] == 0 or board[x+1][y] == 2:
            x += 1
        else:
            check = False
    for i in range(10):
        for j in range(10):
            print(board[i][j], end =' ')
        print('')
```
