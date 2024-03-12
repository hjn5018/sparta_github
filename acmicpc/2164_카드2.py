# N = int(input())

# cards = []
# for i in range(1, N+1):
#     cards.append(i)
# # print(cards)
# # [1, 2, 3, 4, 5, 6]
    
# for _ in range(N-1):
#     cards.pop(0)
#     cards.append(cards.pop(0))
# # cards.pop(0)
# # print(cards)
# # [2, 3, 4, 5, 6]
    
# # print(cards.pop(0))
# # 1

# # cards.pop(0)
# # cards.append(cards.pop(0))
# # print(cards)
# # [3, 4, 5, 6, 2]

# print(cards)
# # [4]

# # 시간 초과
# ========================================
# import sys
# # N = int(input())
# N = int(sys.stdin.readline())

# cards = []
# for i in range(1, N+1):
#     cards.append(i)
# # print(cards)
# # [1, 2, 3, 4, 5, 6]
    
# for _ in range(N-1):
#     cards.pop(0)
#     cards.append(cards.pop(0))
# # cards.pop(0)
# # print(cards)
# # [2, 3, 4, 5, 6]
    
# # print(cards.pop(0))
# # 1

# # cards.pop(0)
# # cards.append(cards.pop(0))
# # print(cards)
# # [3, 4, 5, 6, 2]

# # print(cards)
# # [4]
# sys.stdout.write(f"{cards}")
# # 시간 초과
# ==========================================
# import sys

# N = int(sys.stdin.readline())

# cards = []
# for i in range(1, N+1):
#     cards.append(i)
    
# for _ in range(N-1):
#     cards.pop(0)
#     cards.append(cards.pop(0))

# sys.stdout.write(f"{cards}")
# 시간 초과 // pypy3도 시간초과
# ===========================================
# N = int(input())

# cards = []
# for i in range(1, N+1):
#     cards.append(i)
    
# # for _ in range(N-1):
# #     cards.pop(0)
    
# # cards[0] = cards[5]
# # [6, 2, 3, 4, 5, 6]

# # cards[6] = cards[0]
# # IndexError: list assignment index out of range

# print(cards)
# ==============================================
# N = int(input())

# cards = []
# for i in range(1, N+1):
#     cards.append(i)

# for _ in range(N-1):
#     del cards[0]
# # del cards[0]
# # print(cards)
# # [2, 3, 4, 5, 6]
#     cards.append(cards.pop(0))

# print(cards)
# # 시간 초과
# =========================================
from collections import deque

N = int(input())

cards = deque([x for x in range(1, N + 1)])

for _ in range(N-1):
    cards.popleft()
    # print(cards.popleft())
    # 1
    cards.append(cards.popleft())

# print(cards)
# deque([4])
print(cards[0])
# 4

# 야호!