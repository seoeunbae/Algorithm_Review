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
