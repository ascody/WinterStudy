## Trie

![](https://cdn-images-1.medium.com/max/720/1*MlPQMea_Hc1tNQK3zS0ubg.png)

### 트라이 (Trie)

> **문자열을 저장하고 효율적으로 탐색하기 위한 트리 형태의 자료구조**

#### 목적

- 검색어 자동완성, 사전 찾기, 문자열 검사 등

#### 시간 복잡도
> 제일 긴 문자열의 길이 L
> 총 문자열들의 수 M

- 생성 시간 복잡도 : O(M*L)
- 탐색 시간 복잡도: O(L)

#### 코드 - 삽입 / 검색

```python
class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}

class Trie(object):
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        curr_node = self.head
        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)
            curr_node = curr_node.children[char]
        curr_node.data = string

    def search(self, string):
        curr_node = self.head
        for char in string:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return False
        if curr_node.data != None:
            return True
```

<br>

> **참고**<br>
> [210126 개발일지(50일차) - 트라이(Trie) 알고리즘 개념 및 파이썬에서 구현하기(feat. Class)](https://velog.io/@gojaegaebal/210126-%EA%B0%9C%EB%B0%9C%EC%9D%BC%EC%A7%8050%EC%9D%BC%EC%B0%A8-%ED%8A%B8%EB%9D%BC%EC%9D%B4Trie-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EA%B0%9C%EB%85%90-%EB%B0%8F-%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%97%90%EC%84%9C-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0feat.-Class)<br>
> [Trie: An Efficient Data Structure for String Processing](https://www.enjoyalgorithms.com/blog/introduction-to-trie-data-structure)