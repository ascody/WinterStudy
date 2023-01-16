## Binary Search Tree

<img src="https://blog.kakaocdn.net/dn/bCe3QD/btq2ytHuN1Z/Ai82KHYBlgY01j9hbwjOO1/img.png" width=80%>

### 이진 탐색 트리 (Binary Search Tree, BST)
> 왼쪽 자식 트리에는 자신보다 작은 값, 오른쪽은 자신보다 큰 값으로 정렬한 이진트리

- 노드의 왼쪽 하위 트리에는 **노드의 키보다 작은 키가있는 노드**만 포함

- 노드의 오른쪽 하위 트리에는 **노드의 키보다 큰 키가있는 노드**만 포함

- 왼쪽 및 오른쪽 하위 트리도 각각 이진 검색 트리

- 중복된 키를 허용하지 않음

- **중위 순회를 이용하여 모든 키를 정렬된 순서로 가져올 수 있음**

### 생성과 삽입
<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FmiB91%2Fbtq2DsUG16h%2FZBlqV9bktKWCSDfIfQYxT1%2Fimg.png" width=70%>

```python
# 노드 생성
class Node: # 노드 클래스
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
        
class BinarySearchTree(Node):
    # 노드 삽입
    def insert(self, data):
        self.root = self._insert_value(self.root, data)
        return self.root is not None

    def _insert_value(self, node, data):
        # node (self.root) 가 초기화 되어있지 않으면
        if node is None:
            node = Node(data)
        else:
            # 부모노드와 크기 비교 (재귀)
            if data <= node.data:
                node.left = self._insert_value(node.left, data)
            else:
                node.right = self._insert_value(node.right, data)
        return node
```

### 검색
<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbDH5Xq%2Fbtq2D4F3nRp%2FUFt8cFNCzqfeytVgtvVLuk%2Fimg.png" width=70%>

```python
    # 노드 탐색
    def find(self, key):
        return self._find_value(self.root, key)

    def _find_value(self, root, key):
        if root is None or root.data == key:
            return root is not None
        elif key < root.data:
            return self._find_value(root.left, key)
        else:
            return self._find_value(root.right, key)
```

### 삭제

#### 삭제할 노드가 리프노드인 경우
<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FeudyFG%2Fbtq2GXflqdC%2FTvIXkjTgEWoVoyvOv4xQN1%2Fimg.png" width=70%>

#### 삭제할 노드에 자식이 하나인 경우
<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fd9YABr%2Fbtq2y4HJBqp%2FDbafbadT1SL5WSnKO6AFLK%2Fimg.png" width=70%>

#### 삭제할 노드에 자식이 둘인 경우
<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FkYDgz%2Fbtq2BCDKWPR%2FT5wAjm1PwyAAKq9NNYctV0%2Fimg.png" width=70%>

```python
    # 노드 삭제
    def delete(self, key):
        self.root, deleted = self._delete_value(self.root, key)
        return deleted

    def _delete_value(self, node, key):
        if node is None:
            return node, False

        deleted = False
        # 해당 노드가 삭제할 노드일 경우
        if key == node.data:
            deleted = True
            # 삭제할 노드가 자식이 두개일 경우
            if node.left and node.right:
                # 오른쪽 서브 트리에서 가장 왼쪽에 있는 노드를 찾고 교체
                parent, child = node, node.right
                while child.left is not None:
                    parent, child = child, child.left
                child.left = node.left
                if parent != node:
                    parent.left = child.right
                    child.right = node.right
                node = child
            # 자식 노드가 하나일 경우 해당 노드와 교체
            elif node.left or node.right:
                node = node.left or node.right
            # 자식 노드가 없을 경우 그냥 삭제
            else:
                node = None
        elif key < node.data:
            node.left, deleted = self._delete_value(node.left, key)
        else:
            node.right, deleted = self._delete_value(node.right, key)
        return node, deleted
```

### 시간 복잡도

- 균등 트리 : 노드 개수가 N개일 때 O(logN)

- 편향 트리 : 노드 개수가 N개일 때 O(N)

> 삽입, 검색, 삭제 시간복잡도는 트리의 Depth에 비례


<br>

> **참조**   
> [[자료구조] 이진탐색트리 (Binary Search Tree)](https://github.com/gyoogle/tech-interview-for-developer/blob/master/Computer%20Science/Data%20Structure/Binary%20Search%20Tree.md)   
> [[자료구조] 이진 탐색 트리 (BST, Binary Search Tree)](https://yoongrammer.tistory.com/71)   
> [[Python] 이진 탐색 트리(Binary Search Tree)](https://gingerkang.tistory.com/86)   
