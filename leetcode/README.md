# [Leetcode_no.52] unique_paths
- 난이도 : Medium
- 링크 : https://leetcode.com/problems/unique-paths/

<br/>

## 62.Unique paths
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
