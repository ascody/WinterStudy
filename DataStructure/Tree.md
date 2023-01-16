## Tree

<img src="https://miro.medium.com/max/677/1*Z89j_NoDx9HkFcPHy3rPZg.png" width="40%">

### 트리(Tree)란
> <b>정점(node)와 간선(edge)을 이용하여 데이터의 배치 형태를 추상화한 자료구조</b>

- 노드가 N개인 트리는 항상 N-1개의 간선(edge)을 가진다.<br>
    -> 간선은 항상 (정점의 개수 - 1) 만큼을 가진다.

- 루트에서 어떤 노드로 가는 경로는 유일하다. 또한 임의의 두 노드 간의 경로도 유일하다.<br>
    -> 두 개의 정점 사이에 반드시 1개의 경로만을 가진다

- 모든 자식 노드는 하나의 부모 노드만을 가진다.

### 용어 설명

<img src="https://gmlwjd9405.github.io/images/data-structure-tree/tree-terms.png" width="40%">
<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fc21sKi%2FbtraMphuVNk%2Figctr5jMswnomHAIrnKvGk%2Fimg.png" width="50%">
<br><br>

* 노드(Node): 트리에서 데이터를 저장하는 기본 요소로, Branch 정보 또한 포함
* 간선(Edge): 노드와 노드를 연결하는 연결선
* 루트 노드(root node): 부모가 없는 노드, 트리는 하나의 루트 노드만을 가진다.
* 단말 노드(leaf node): 자식이 없는 노드, ‘말단 노드’ 또는 ‘잎 노드’라고도 부른다.
* 내부(internal) 노드: 단말 노드가 아닌 노드
* 간선(edge): 노드를 연결하는 선 (link, branch 라고도 부름)
* 형제(sibling): 같은 부모를 가지는 노드
* 노드의 크기(size): 자신을 포함한 모든 자손 노드의 개수
* 노드의 깊이(depth): 루트에서 어떤 노드에 도달하기 위해 거쳐야 하는 간선의 수
* 노드의 레벨(level): 트리의 특정 깊이를 가지는 노드의 집합
* 노드의 차수(degree): 하위 트리 개수 / 간선 수 (degree) = 각 노드가 지닌 가지의 수
* 트리의 차수(degree of tree): 트리의 최대 차수
* 트리의 높이(height): 루트 노드에서 가장 깊숙히 있는 노드의 깊이

### 트리 순회 방식

<img src="https://global-uploads.webflow.com/5d0dc87aac109e1ffdbe379c/60e18e09daeb6db6f4995305_-Vsv_RLYEukjbDMgKxKJpxTnA246o-X1OjUPkl5HvnSiR-dFU4w5qKNaUtw-rq8wD4vMTGxFKtjvKCt7Uthmidpl_ajqRpVqgAH57N1HTpQ5MGBE4HCvE0dq7gTeM4-JtFLkQShX.png" width="40%">

#### 전위 순회(pre-order)
> 루트를 먼저 방문하는 방식 **(Root -> 왼쪽 자식 -> 오른쪽 자식)**

#### 중위 순회(in-order)
> 왼쪽 하위 트리를 방문 후 루트를 방문하는 방식 **(왼쪽 자식 -> Root -> 오른쪽 자식)**

#### 후위 순회(post-order)
> 하위를 모두 방문 후 루트를 방문하는 방식 **(왼쪽 자식-> 오른쪽 자식 -> Root)**

#### 레벨 순회(level-order)
> 루트 노드를 먼저 탐색하고, 그 다음 레벨의 노드를 탐색하는 방식

### 이진트리의 종류

![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FGRP0C%2FbtqEYaoOINE%2FLfrvfpfNpHj60outC3zMMk%2Fimg.png)

#### 이진트리 (Binary Tree)
> 최대 두 개의 자식을 갖는 트리

#### 포화 이진트리 (Full Binary Tree)
> 노드들이 자식 요소를 두 개를 가지거나, 한개도 가지지 않는 이진트리

#### 완전 이진트리 (Complete Binary Tree)
> 모든 레벨의 자식이 왼쪽부터 채워지는 이진트리

#### 변질 이진트리 (Degenerate Binary Tree)
> 모든 부모 노드가 왼쪽으로 자식을 갖는 이진트리

#### 정 이진트리 (Perfet Binary Tree)
> 노드들의 자식요소를 모두 두개 가지고 있는 이진트리

#### 균형 이진트리 (Balanced Binary Tree)
> 모든 노드의 왼쪽과 오른쪽 하위 트리의 높이가 최대 1만큼 차이가 날 수 있는 이진 트리

### 이진 검색 트리 (BST : Binary Search Tree)
![](https://velog.velcdn.com/images%2Fvermonter%2Fpost%2F691e0ee8-50d3-4f25-9042-6fb4f0afdcba%2Fimage.png)
> 왼쪽 자식 트리에는 자신보다 작은 값, 오른쪽은 자신보다 큰 값으로 정렬한 이진트리

<br><br>

> **참조**<br>
> [대표적인 자료구조: 트리](https://www.fun-coding.org/Chapter10-tree.html#gsc.tab=0)<br>
> [[자료구조] 트리(Tree) (Python)](https://tipsyziasu.tistory.com/94)<br>
> [[파이썬 자료구조] :: 트리 (Tree)](https://m.blog.naver.com/leeinje66/221622228795)<br>
> [[자료구조] 트리(Tree)란](https://gmlwjd9405.github.io/2018/08/12/data-structure-tree.html)<br>
> [[자료 구조] - 트리 자료 구조 (3)-이진 트리와 종류(완전, 포화, 완벽, 균형) :: Binary Tree (Full, Complete, Perfect, Balanced)](https://wonit.tistory.com/198)<br>
> [5-2. [자료구조] 이진트리(binary tree)](https://kingpodo.tistory.com/27)<br>
> [[tech-interview-for-developer] Tree](https://github.com/gyoogle/tech-interview-for-developer/blob/master/Computer%20Science/Data%20Structure/Tree.md)<br>
> [[Data Structure] 이진 트리(Binary Tree)의 세 가지 종류와 특징](https://velog.io/@vermonter/Data-Structure-%EC%9D%B4%EC%A7%84-%ED%8A%B8%EB%A6%ACBinary-Tree%EC%9D%98-%EC%84%B8-%EA%B0%80%EC%A7%80-%EC%A2%85%EB%A5%98%EC%99%80-%ED%8A%B9%EC%A7%95)<br>
> [이진 트리 순회: 전위, 중위, 후위, 레벨](https://www.jiwon.me/binary-tree-traversal/)
