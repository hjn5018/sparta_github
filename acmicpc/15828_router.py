import sys
from collections import deque

# sys.stdin = open('input.txt')

N = int(sys.stdin.readline())

router = deque()
# print(router)
# deque([])

# router = [0]*N
# print(router)
# [0, 0, 0, 0, 0]

while True:
    # info = int(input())
    # EOFError: EOF when reading a line
    
    info = int(sys.stdin.readline())
# ValueError: invalid literal for int() with base 10: ''
# ValueError: invalid literal for int() with base 10: '\n'
# ValueError: could not convert string to float: ''

    # if # 큐가 비어있는데 ~~
    
    if info == 0:
        router.popleft()
    elif info == -1:
        break
    # continue를 포함한 분기가 break위에 있어서 예제 입력 2에서 오류가 났나?
    elif len(router) == N:
        # pass
        continue
    else:
        router.append(info)

# print(router)
# deque([])

if router == deque():
    print('empty')
else:
    # for i in range(len(router)):
    #     router[i] = str(router[i])
    # result = " ".join(router)
    result = " ".join([str(x) for x in router])
# TypeError: sequence item 0: expected str instance, int found
    print(result)
# 5 6
    # print(" ".join([str(x) for x in router]))

# 100점이지만 뭔가 께름칙한게.. deque에 아무것도 없는데 popleft하면 무슨 일이 일어나나..
# ==================================
# from collections import deque

# d = deque()
# # print(d)
# # deque([])

# d.popleft()
# # ??

# print(d.popleft())
# IndexError: pop from an empty deque
# ??? 그냥 popleft()하면 괜찮아보이는데, print()하면 이러네....