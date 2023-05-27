
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