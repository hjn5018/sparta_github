# heapq 구현해서 해보기# heapq 구현해서 해보기# heapq 구현해서 해보기# heapq 구현해서 해보기# heapq 구현해서 해보기
"""
9
0
12345678
1
2
0
0
0
0
32
"""

# list_ = []

# N = int(input())

# # for _ in range(N):
# # N번 하는 게 아니야!
#     x = int(input())

#     if x > 0:
#         list_.append(x)
#     else:
#         try:
#             print(list_.pop(min(list_)))
#         except ValueError: # 배열이 비어있는데 가장 작은 값을 출력할 경우 0 출력
#             print("0")

# list_A = [1, 2, 3, 4]
# print(list_A.pop())
# print(list_A)
# 4
# [1, 2, 3]
            
# 9                           
# 0
# 0
# 12345678
# 1
# 2
# 0
# 1
# 0
# Traceback (most recent call last):
#   File "1927_최소_힙.py", line 12, in <module>
#     print(list_.pop(min(list_)))
# IndexError: pop index out of range
# ========================================================
# list_ = []

# N = int(input())

# # for _ in range(N):
# # N번 하는 게 아니야!
# while 1:
#     x = int(input())

#     if x > 0:
#         list_.append(x)
#     else:
#         try:
#             print(list_.pop(min(list_)))
#             # IndexError: pop index out of range
#             # 아..? pop의 매개변수는 index구나
#             # 그럼 리무브를 쓸까?
#         except ValueError: # 배열이 비어있는데 가장 작은 값을 출력할 경우 0 출력
#             print("0")
# ==========================================================
# list_ = []

# N = int(input())

# # for _ in range(N):
# # N번 하는 게 아니야!
# while 1:
#     x = int(input())

#     if x > 0:
#         list_.append(x)
#     else:
#         try:
#             print(list_[-1])
#             # IndexError: list index out of range
#             list_.remove(min(list_))
#             # print(list_.pop(min(list_)))
#             # IndexError: pop index out of range
#             # 아..? pop의 매개변수는 index구나
#             # 그럼 리무브를 쓸까?
#         except ValueError: # 배열이 비어있는데 가장 작은 값을 출력할 경우 0 출력
#             print("0")
# =========================================================
# # list_ = []

# N = int(input())

# # for _ in range(N):
# # N번 하는 게 아니야!
# while 1:
#     x = int(input())

#     if x > 0:
#         list_.append(x)
#     else:
#         try:
#             print(list_[-1:-1:-1])
#             # IndexError: list index out of range
#             list_.remove(min(list_))

#         except ValueError: # 배열이 비어있는데 가장 작은 값을 출력할 경우 0 출력
#             print("0")
# =====================================================
# import heapq

# list_ = []
# # list_.heapify()

# N = int(input())

# # for _ in range(N):
# # N번 하는 게 아니야!
# while 1:
#     x = int(input())

#     if x > 0:
#         list_.heappush(x)
#         # AttributeError: 'list' object has no attribute 'heappush'
#     else:
#         try:
#             print(list_[-1:-1:-1])
#             # IndexError: list index out of range
#             list_.remove(min(list_))

#         except ValueError: # 배열이 비어있는데 가장 작은 값을 출력할 경우 0 출력
#             print("0")
# =========================================================
# import heapq

# list_ = []
# # list_.heapify()

# N = int(input())

# # for _ in range(N):
# # N번 하는 게 아니야!
# while 1:
#     x = int(input())

#     if x > 0:
#         # list_.heappush(x)
#         heapq.heappush(list_, x)
#         # AttributeError: 'list' object has no attribute 'heappush'
#     else:
#         try:
#             print(list_[-1:-1:-1])
#             # IndexError: list index out of range
#             heapq.heappop(list_, )

#         except ValueError: # 배열이 비어있는데 가장 작은 값을 출력할 경우 0 출력
#             print("0")

# # heapq 사용이 안 돼 ㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠ
# # $ pip install heapq
# # ERROR: Could not find a version that satisfies the requirement heapq (from versions: none)
# # ERROR: No matching distribution found for heapq
# # ?????????????????????????///
            
# # heapq 구현해서 해보기
# ==================================================
# import heapq

# list_ = []
# N = int(input())

# for _ in range(N):
#     x = int(input())
#     if x > 0:
#         heapq.heappush(list_, x)
#     else: # x = 0인 경우
#         if list_ == []:
#             print(0)
#         else:
#             print(heapq.heappop(list_))
# 시간 초과?????????????????????????????//

    # if x > 0:
    #     heapq.heappush(list_, x)
    # else: # x == 0
    #     try:
    #         # 배열에서 가장 작은 값을 출력하고 그 값을 배열에서 제거
    #         heapq.heappop(list_)
    #     except ValueError: # 배열에 아무런 값이 없을 경우
    #         print(0)

# ======================================
# print(bool([]))
# False
# print(bool([1]))
# True
# =============================================
# import heapq

# list_ = []
# N = int(input())

# for _ in range(N):
#     x = int(input())
#     if x > 0:
#         heapq.heappush(list_, x)
#     elif list_ and x == 0:
#         print(heapq.heappop(list_))
#     else: # list_가 비어있을 경우
#         print(0)
# 시간 초과?????????????????????????????????????????
        
# import heapq

# list_ = []
# N = int(input())

# for _ in range(N):
#     x = int(input())
#     if x > 0:
#         heapq.heappush(list_, x)
#     else: # x = 0인 경우
#         if list_ == []:
#             print(0)
#         else:
#             print(heapq.heappop(list_))
# ======================================================
# import heapq, sys
# list_ = []
# N = int(sys.stdin.readline())

# for _ in range(N):
#     x = int(sys.stdin.readline())
#     if x > 0:
#         heapq.heappush(list_, x)
#     elif list_ and x == 0:
#         sys.stdout.write(f"{heapq.heappop(list_)}")
#     else: # list_가 비어있을 경우
#         sys.stdout.write(f"0")
# 9
# 0
# 12345678
# 1
# 2
# 0
# 0
# 0
# 0
# 32
# 012123456780
# ==============================
# import heapq, sys
# list_ = []
# N = int(sys.stdin.readline())

# for _ in range(N):
#     x = int(sys.stdin.readline())
#     if x > 0:
#         heapq.heappush(list_, x)
#     elif list_ and x == 0:
#         sys.stdout.write(f"{heapq.heappop(list_)}\n")
#     else: # list_가 비어있을 경우
#         sys.stdout.write(f"0")
# 9
# 0
# 12345678
# 1
# 2
# 0
# 01
# 0
# 2
# 0
# 12345678
# 0
# 32
# 0
# 틀렸습니다.
# =================================
import heapq
list_ = []
N = int(input())

for _ in range(N):
    x = int(input())
    if x > 0:
        heapq.heappush(list_, x)
    elif list_ and x == 0:
        print(heapq.heappop(list_))
    else: # list_가 비어있을 경우
        print(0)