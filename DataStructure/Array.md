## 배열 (Array)

![](https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Array1.svg/330px-Array1.svg.png)

<br>

> <b>번호(인덱스)와 번호에 대응하는 데이터들로 이루어진 자료 구조</b>

![](https://blog.kakaocdn.net/dn/cpugXJ/btqI9owATgF/Kjhgn7ubHy5ITWwMgCErv1/img.png)

```Python
    '''
    인덱스(index): 배열에서의 위치를 가리키는 숫자
    배열의 인덱스는 0부터 시작
    '''
    # 1차원 배열
    arr1 = [0, 0, 0, 0]
    # 2차원 배열
    arr2 = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
        ]

    '''
    정적 배열
    - 배열의 크기가 정해져 있는 배열
    - 한번 생성하면 크기를 변경할 수 없음

    동적 배열
    - 크기를 자동으로 조절하는 배열
    - 저장 공간이 가득 차는 경우 자동적으로 사이즈를 늘려 데이터 추가가 가능
    '''
    # 파이썬의 배열은 동적 배열
    arr1 = [0, 0, 0, 0]
    arr2 = [1, 1, 1]

    arr2.append(1) # [1, 1, 1, 1]
    arr3 = arr1.extend(arr2) #  [0, 0, 0, 0, 1, 1, 1, 1]
    arr2.insert(0, 1) # arr.insert(index, value) -> [1, 1, 1, 1, 1]
    del arr2[0] # del arr[index] -> [1, 1, 1, 1]
```
