# 알고리즘 리뷰 프로젝트 1-Week(5/27)

## [Leetcode_62] Unique paths
- 난이도 : Medium
- 링크 : https://leetcode.com/problems/unique-paths/

<br/>

<details>
<summary>문제 설명</summary>
<div markdown="1">

### 문제 설명

There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

<br/>
<br/>

Example 1:

<img width="442" alt="image" src="https://github.com/seoeunbae/Algorithm_Review/assets/71380240/42ec6607-ae9a-4cd8-96e5-40fb782a6f5b">

<br/>
<br/>

```
Input: m = 3, n = 7
Output: 28
```

</div>
</details>

## 1. DFS로 풀이하는 경우

```python
def unique_paths_with_dfs(self, m: int, n: int) -> int:
    board = [[0 for i in range(n)] for j in range(m)]
    dx = [0, 1]
    dy = [1, 0]
    queue = [(0, 0)]

    while queue:
        x, y = queue.pop()
        board[x][y] += 1
        for k in range(2):
            bx = x + dx[k]
            by = y + dy[k]
            if 0 <= bx < n and 0 <= by < n:
                queue.append((bx, by))

    return board[m - 1][n - 1]
# Time Limit Exceeded

```

해당 문제에서 이동가능한 방향은 "down", "right" 만 존재한다.
시작지점은 항상 (0,0) 으로 동일하다.
보드를 0으로 초기화해준 상태에서 ```중복가능``` 하게, 특정 위치를 지나가는 경우 +1을 해주면,
해당 위치를 visit 하게되는 경우의 수가 나오고 이 값은 특정위치까지 가게되는 경우의 수와 동일하다.
리턴값은 (m-1,n-1)의 위치의 값을 반환하게되면 경우의 수가 나온다.

<br/>

## 2. DP로 풀이하는 경우

```python
def unique_paths_with_dp(self, m: int, n: int):
    board = [[0 for i in range(n)] for j in range(m)]
    for i in range(n):
        board[0][i] = 1
    for i in range(m):
        board[i][0] = 1

    for i in range(1,n):
        for j in range(1,m):
            board[j][i] = board[j-1][i] + board[j][i-1]

    return board[m-1][n-1]
# Runtime - 41ms
```

동일하게 보드를 0으로 초기화해준다.
```(m,n)의 값 = 왼쪽(m-1,n)에서 오는값 + 위(m,n-1)에서 내려오는 값 ``` 이라는 규칙을 발견한다.
첫행렬은 전부 1이 되므로, 초기화해준다.
(mxn)보드를 돌면서 값을 채워준다.

<br/>

## [2022kakaointernship] 두큐합 같게 만들기

난이도 : LV.3

링크 : https://school.programmers.co.kr/learn/courses/30/lessons/118667

<br/>

<details>
<summary>문제 설명</summary>
<div markdown="1">



### 문제 설명

길이가 같은 두 개의 큐가 주어집니다. 하나의 큐를 골라 원소를 추출(pop)하고, 추출된 원소를 다른 큐에 집어넣는(insert) 작업을 통해 각 큐의 원소 합이 같도록 만들려고 합니다. 이때 필요한 작업의 최소 횟수를 구하고자 합니다. 한 번의 pop과 한 번의 insert를 합쳐서 작업을 1회 수행한 것으로 간주합니다.
큐는 먼저 집어넣은 원소가 먼저 나오는 구조입니다. 이 문제에서는 큐를 배열로 표현하며, 원소가 배열 앞쪽에 있을수록 먼저 집어넣은 원소임을 의미합니다. 즉, pop을 하면 배열의 첫 번째 원소가 추출되며, insert를 하면 배열의 끝에 원소가 추가됩니다. 예를 들어 큐 [1, 2, 3, 4]가 주어졌을 때, pop을 하면 맨 앞에 있는 원소 1이 추출되어 [2, 3, 4]가 되며, 이어서 5를 insert하면 [2, 3, 4, 5]가 됩니다.
다음은 두 큐를 나타내는 예시입니다.

<br/>

```
queue1 = [3, 2, 7, 2]
queue2 = [4, 6, 5, 1]
```
<br/>

두 큐에 담긴 모든 원소의 합은 30입니다. 따라서, 각 큐의 합을 15로 만들어야 합니다. 예를 들어, 다음과 같이 2가지 방법이 있습니다.
<br/>
1. queue2의 4, 6, 5를 순서대로 추출하여 queue1에 추가한 뒤, queue1의 3, 2, 7, 2를 순서대로 추출하여 queue2에 추가합니다. 그 결과 queue1은 [4, 6, 5], queue2는 [1, 3, 2, 7, 2]가 되며, 각 큐의 원소 합은 15로 같습니다. 이 방법은 작업을 7번 수행합니다.
2. queue1에서 3을 추출하여 queue2에 추가합니다. 그리고 queue2에서 4를 추출하여 queue1에 추가합니다. 그 결과 queue1은 [2, 7, 2, 4], queue2는 [6, 5, 1, 3]가 되며, 각 큐의 원소 합은 15로 같습니다. 이 방법은 작업을 2번만 수행하며, 이보다 적은 횟수로 목표를 달성할 수 없습니다.
<br/>

따라서 각 큐의 원소 합을 같게 만들기 위해 필요한 작업의 최소 횟수는 2입니다.
길이가 같은 두 개의 큐를 나타내는 정수 배열 queue1, queue2가 매개변수로 주어집니다. 각 큐의 원소 합을 같게 만들기 위해 필요한 작업의 최소 횟수를 return 하도록 solution 함수를 완성해주세요. 단, 어떤 방법으로도 각 큐의 원소 합을 같게 만들 수 없는 경우, -1을 return 해주세요.
<br/>

### 제한사항

```
1 ≤ queue1의 길이 = queue2의 길이 ≤ 300,000
1 ≤ queue1의 원소, queue2의 원소 ≤ 109
주의: 언어에 따라 합 계산 과정 중 산술 오버플로우 발생 가능성이 있으므로 long type 고려가 필요합니다.
```
<br/>

### 입출력 예
|queue1|queue2|result|
|------|------|-------|
|[3, 2, 7, 2]|[4, 6, 5, 1]|2|
|[1, 2, 1, 2]|[1, 10, 1, 2]|7|
|[1, 1]|[1, 5]|-1|

<br/>



</div>
</details>

## 구현 풀이

```python
from collections import deque

def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)

    queue1_sum = sum(queue1)
    queue2_sum = sum(queue2)
    total_sum = queue1_sum + queue2_sum

    if total_sum % 2 == 1:
        return -1


    execute = 0
    count = 0
    while queue1_sum != queue2_sum:
        execute += 1
        # 시간초과 방지하기
        if execute > 599999:
            return -1

        if queue1 and queue1_sum > queue2_sum:
            poped = queue1.popleft()
            queue2.append(poped)
            count+=1
            queue1_sum -= poped
            queue2_sum += poped
        elif queue2 and queue2_sum > queue1_sum:
            poped = queue2.popleft()
            queue1.append(poped)
            count+=1
            queue1_sum += poped
            queue2_sum -= poped

    return count

```

<br/>

deque의 ```popleft()```가 queue의 ```pop()```보다 성능이 좋으므로, deque에 넣어준다.<br/>
각 큐의 합과 총 합을 구한뒤, 총합이 홀수라면 두큐가 동일한 합을 가질수없으므로, ```-1```을 반환한다.<br/>
두 큐의 합이 같아질 때까지, 큰 큐의 원소를 pop하고, 작은 큐에게 append하는 과정을 한번씩, 반복한다.<br/>
테스트 케이스 11,28이 시간초과가 나는 이슈를 방지하기 위해, ```while실행 횟수 > queue최대길이 * 2```인 경우, 역시 -1을 리턴한다.<br/>
마지막으로 팝했던 경우의 횟수를 리턴해준다.

<br/>

### 최악의 경우 예시
<br/>

```
queue1 = {1,1,1,1,.... 1} (30만개)
queue2 = {1,1,1,1,.....,599999, 1} (30만개)
```
<br/>
```
worstLoop = len(queue1) * 3

while( loop <= worstLoop){
    ...
}
```



- 다른 풀이1 : queue배열 그대로와, 피벗을 사용하는 방
    - pivot 이 range를 초과하는 경우! pivot은 상대 배열로 넘어간다.
    - 전체를 한바퀴 도는 경우 => ```len(queue) * 4``` 이다.
- 다른 풀이2 : 투포인터 방식
    - 하나의 배열로 합친 뒤, 시작포인터와 끝포인터를 설정한다.
      - 한 큐의 합이, 총합의 반이면 충족하게된다.
      - 작으면 끝포인터를 ++, 크면 시작포인터를 ++ 한다.
      - 움직이는 횟수가 pop/append횟수가 된다.

 
      