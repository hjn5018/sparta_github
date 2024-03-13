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
