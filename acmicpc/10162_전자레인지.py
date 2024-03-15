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
        if T >= 5*60:
            a += 1
            T -= 500
            continue
        if T >= 60:
            b += 1
            T -= 60
            continue
        if T >= 10:
            c += 1
            T -= 10
            
    print(f"{a} {b} {c}")