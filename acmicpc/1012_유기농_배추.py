# import sys

# T = int(sys.stdin.readline())
# M, N, K = map(int, sys.stdin.readline())

# # 상하좌우 = [(0, 1), (0, -1), (-1, 0), (1, 0)]
# 상하좌우 = [[0, 1], [0, -1], [-1, 0], [1, 0]]
# for _ in range(T):
#     farm = []
#     for _ in range(K):
#         pos = list(map(int, sys.stdin.readline().split()))
#         farm.append(pos)
#     memoi = []
#     for i in range(K):
#         if farm[i] not in memoi:
#             memoi.append(farm[i])
#             for j in range(len(상하좌우)):
#                 farm[i] += 상하좌우[j]
#                 if farm[i] in farm:
#                     farm.append(farm[i])
# memoi를 쓰려고해도 O(j^i)는 좀 아니지 않나..?
# =====================================================
# 한결 튜터님 세션 -> BFS로 풀어보세요!

# import sys
# from collections import deque
# from pprint import pprint

# # sys.stdin = open('input.txt')

# T = int(sys.stdin.readline())

# 상하좌우 = [[0, 1], [0, -1], [-1, 0], [1, 0]]

# def bfs(i, j):
#     farm[j][i] = 0

#     # 상하좌우 탐색
#     for dx, dy in 상하좌우:
#         nx = j + dx
#         ny = i + dy

#         if (nx < 0) or (ny < 0) or (nx > M) or (ny > N):
#             continue
#         if farm[nx][ny] == 1:
            


# for _ in range(T):
#     M, N, K = map(int, sys.stdin.readline().split())
#     farm = [[0]*M for _ in range(N)]
#     # print([[0]*3 for _ in range(2)])
#     # [[0, 0, 0], [0, 0, 0]]
    
#     # pprint(farm)
#     # [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     #  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     #  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     #  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     #  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     #  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     #  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     #  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    
#     for _ in range(K):
#         x, y = map(int, sys.stdin.readline().split())
#         farm[y][x] = 1
#     # pprint(farm)
#     # [[1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
#     # [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
#     # [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
#     # [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
#     # [0, 0, 1, 1, 0, 0, 0, 1, 1, 1],
#     # [0, 0, 0, 0, 1, 0, 0, 1, 1, 1],
#     # [0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
#     # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

#     # [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     # [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
#     # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
#     count = 0
#     for i in range(N):
#         for j in range(M):
#             bfs(i, j)
#             count += 1
# =================================================
import sys
from collections import deque
# from pprint import pprint

sys.stdin = open('input.txt')

T = int(sys.stdin.readline())

상하좌우 = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def bfs(i, j):
    queue = deque()
    queue.append([i, j])
    while queue: # True:
        queue.popleft()
        for di, dj in 상하좌우:
            ni = i + di
            nj = j + dj

            if (ni < 0) or (nj < 0) or (ni > N) or (nj > M):
                continue

            if farm[ni][nj] == 1:
                # IndexError: list index out of range
                queue.append([ni, nj])
                farm[ni][nj] = 0


for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    farm = [[0]*M for _ in range(N)]
    # print([[0]*3 for _ in range(2)])
    # [[0, 0, 0], [0, 0, 0]]
    
    # pprint(farm)
    # [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    
    for _ in range(K):
        X, Y = map(int, sys.stdin.readline().split())
        farm[Y][X] = 1
    # pprint(farm)
    # [[1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    # [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    # [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    # [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    # [0, 0, 1, 1, 0, 0, 0, 1, 1, 1],
    # [0, 0, 0, 0, 1, 0, 0, 1, 1, 1],
    # [0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    # [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    # [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    count = 0
    for i in range(N):
        for j in range(M):
            if farm[i][j] == 1:
                bfs(i, j)
                count += 1

    print(count)