# import sys

# T = int(sys.stdin.readline())


# for _ in range(T):
#     C = int(sys.stdin.readline())

#     coin_list = [0, 0, 0, 0]
#     while C:
#         if C >= 25:
#             coin_list[0] += 1
#             C -= 25
#             continue
#         elif C >= 10:
#             coin_list[1] += 1
#             C -= 10
#             continue
#         elif C >= 5:
#             coin_list[2] += 1
#             C -= 5
#             continue
#         elif C >= 1:
#             coin_list[3] += 1
#             C -= 1
#             continue

#     result = " ".join(map(str, coin_list))
#     print(f"{result}")
# =================================================
import sys

T = int(sys.stdin.readline())


for _ in range(T):
    C = int(sys.stdin.readline())

    coin_value = [25, 10, 5 ,1]
    coin_list = [0, 0, 0, 0]
    while C:
        if C >= 25:
            coin_list[0] += 1
            C -= 25
            continue
        elif C >= 10:
            coin_list[1] += 1
            C -= 10
            continue
        elif C >= 5:
            coin_list[2] += 1
            C -= 5
            continue
        elif C >= 1:
            coin_list[3] += 1
            C -= 1
            continue

    result = " ".join(map(str, coin_list))
    print(f"{result}")