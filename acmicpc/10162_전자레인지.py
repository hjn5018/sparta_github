# import sys

# T = int(sys.stdin.readline())

# a, b, c = 0, 0, 0

# if T % 10 != 0:
#     print(-1)
# else:
#     while True:
#         if T > 5*60:
#             a += 1
#             T -= 500
#             continue
#         if T > 60:
#             b += 1
#             T -= 60
#             continue
#         if T > 10:
#             c += 1
#             T -= 10
#         if T == 0:
#             break

# print(f"{a} {b} {c}")
# ==============================
# import sys

# T = int(sys.stdin.readline())

# a, b, c = 0, 0, 0

# if T % 10 != 0:
#     print(-1)
# else:
#     while T:
#         if T > 5*60:
#             a += 1
#             T -= 500
#             continue
#         if T > 60:
#             b += 1
#             T -= 60
#             continue
#         if T > 10:
#             c += 1
#             T -= 10

# print(f"{a} {b} {c}")
# =================================================
import sys

T = int(sys.stdin.readline())

a, b, c = 0, 0, 0

if T % 10 != 0:
    print(-1)
else:
    while T:
        if T >= 5*60: # T가 10000까지이므로 최악의 경우에 대비하려면 300분 계속 도는 걸 줄여야함.
            a += 1
            T -= 300 # 왜 내가 500을 뺐지;; 300빼자
            continue
        if T >= 60:
            b += 1
            T -= 60
            continue
        if T >= 10:
            c += 1
            T -= 10
            
    print(f"{a} {b} {c}")
    # T = 350 이면 왜 무한 루프인가..
# ==================================
# import sys

# T = int(sys.stdin.readline())

# a, b, c = 0, 0, 0

# if T % 10 != 0:
#     print(-1)
# else:
#     while T:
#         if T >= 5*60: # T가 10000까지이므로 최악의 경우에 대비하려면 300분 계속 도는 걸 줄여야함.
#             a += T // 300
#             T -= 300 * a
#             continue
#         if T >= 60:
#             b += 1
#             T -= 60
#             continue
#         if T >= 10:
#             c += 1
#             T -= 10
            
#     print(f"{a} {b} {c}")