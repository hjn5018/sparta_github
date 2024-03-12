"""
3
1 0
5
4 2
1 2 3 4
6 0
1 1 9 1 1 1
"""
"""
3
4 2
1 2 3 4
"""


# from collections import deque
# # import sys

# # T = int(sys.stdin.readline())
# T = int(input())

# for _ in range(T):
#     # N, M = map(int, sys.stdin.readline().split())
#     N, M = map(int, input().split())
#     # importance = list(map(int, sys.stdin.readline().split()))
#     # importance = deque(map(int, sys.stdin.readline().split()))
#     importance = deque(map(int, input().split()))

#     # print(importance)
#     # deque([5])

#     # print(max(importance))
# # 3
# # 1 0
# # 5
# # 5
# # 4 2
# # 1 2 3 4
# # 4
# # 6 0
# # 1 1 9 1 1 1
# # 9
#     # count = 0
#     # # for _ in range(N):
#     # # max(importance) == M 가 True 일 때까지 돌아야함
#     # while 1:
#     #     if importance[0] < max(importance):
#     #         # IndexError: deque index out of range

#     #         importance.append(importance.popleft())
#     #     else: # max == [0]
#     #         count += 1
#     #         if max(importance) == M:
#     #             print(count)
#     #             # sys.stdout.write(f"{count}")
#     #             break
#     #         else:
#     #             importance.remove(max(importance))
# =====================================================================
# from collections import deque
# T = int(input())

# for _ in range(1):
#     N, M = map(int, input().split())
#     importance = list(map(int, input().split()))
#     # print(importance)
#     # [5]

#     importance = deque(importance)
# # print(importance)
# # deque([5])

# # max(importance)
# # ????????




#     # count = 0
#     # while 1:
#     #     if importance[0] < max(importance):
#     #         # IndexError: deque index out of range

#     #         importance.append(importance.popleft())
#     #     else: # max == [0]
#     #         count += 1
#     #         if max(importance) == M:
#     #             print(count)
#     #             break
#     #         else:
#     #             importance.remove(max(importance))
# =============================================================
from collections import deque
T = int(input())

for _ in range(1):
    N, M = map(int, input().split())
    importance = list(map(int, input().split()))
    # print(importance)
    # [1, 2, 3, 4]
    max_imp = max(importance)
    
    importance = deque(importance)
# print(importance)
# deque([1, 2, 3, 4])

# max(importance)
# ????????

# print(importance[0])
# 1

# print(max_imp)
# 4


    # count = 0
    # while 1:
    #     if importance[0] < max_imp:
    #         # IndexError: deque index out of range

    #         importance.append(importance.popleft())
    #     else: # max == [0]
    #         count += 1
    #         if max_imp == M:
    #             print(count)
    #             break
    #         else:
    #             importance.remove(max_imp)