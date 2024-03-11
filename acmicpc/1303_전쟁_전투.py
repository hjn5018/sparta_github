# 한결 튜터님 풀이
N, M = map(int, input().split())

board = []
for _ in range(M):
    board.append([s for s in input()])
    # ["W", "B", "W", "W", "W"]

상하좌우 = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def get_checkable_block(row, col, color):
    checkable = []
    for row_add, col_add in 상하좌우:
        target_row = row + row_add
        target_col = col + col_add

        if N > target_col >= 0 and M > target_row >= 0 and board[target_row][target_col] == color:
            checkable.append((target_row, target_col))
    return checkable

def dfs_board(row: int, col:int):
    if board[row][col] == 'X':
        return 0
    color = board[row][col]
    board[row][col] = 'X'
    combo = 1
    checkable_block = get_checkable_block(row, col, color)
    for block_row, block_col in checkable_block:
        combo += dfs_board(block_row, block_col)
    else:
        return combo

scores = [0, 0]
for row in range(M):
    for col in range(N):
        color = board[row][col]
        # W or B
        combo = dfs_board(row,col)
        scores[0 if color == "W" else 1] += combo ** 2

print(scores[0], scores[1])
# ==============================================
# 내가 풀어보자!