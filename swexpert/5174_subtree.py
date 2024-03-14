# import sys

# T = int(sys.stdin.readline())

# for _ in range(1, T+1):
#     E, N = map(int, sys.stdin.readline().split())
#     pair_list = list(map(int, sys.stdin.readline().split()))

#     keys = []
#     values = []
#     for i in range(len(pair_list)):
#         if i % 2 == 0:
#             keys.append(pair_list[i])
#         else:
#             values.append(pair_list[i])
    # print(keys)
    # print(values)
    # [2, 2, 1, 5, 6]
    # [1, 5, 6, 3, 4]

    # pair_dict = {}
    # for i in range(len(keys)):
    #     pair_dict[keys[i]] = values[i]
    # print(pair_dict)
    # {2: 5, 1: 6, 5: 3, 6: 4}
# ============================================================
T = int(input())


def descendant(n):
    global count

    # ch 리스트에 0 또는 []등을 배치했을 때 사용할 수 있는 조건문
    if n:
        count += 1
        descendant(ch1[n])
        descendant(ch2[n])



for i in range(1, T+1):
    E, N = map(int, input().split())
    pair_list = list(map(int, input().split()))
    # print(pair_list)
    # [2, 1, 2, 5, 1, 6, 5, 3, 6, 4]


    # 리스트를 생성한다.
    # 리스트는 Edge + 1 만큼의 Node가 있다.
    # 리스트는 모든 노드를 표현한다.
    # +) 리스트의 인덱스가 노드(1,2,3,4,5,6)를 표현할 수 있도록,
    #    파이썬의 리스트에서 인덱스가 0인 부분을 헤아린다. (E + 1 ---> E + 2)
    ch1 = [0] * (E+2)
    ch2 = [0] * (E+2)
#     print(ch1)
#     print(ch2)
#     [0, 0, 0, 0, 0, 0, 0]
#     [0, 0, 0, 0, 0, 0, 0]

    # for i in range(len(pair_list), 2): 조심하자!!!!!
    for j in range(0, len(pair_list), 2):
        # print(i)
        parent, child = pair_list[j], pair_list[j+1]
        # print(parent, child)
        # ch1 리스트의 '부모' 번째 index에 값이 0이라면 => '자식'의 정보가 담겨있지 않다면
        if ch1[parent] == 0:
            ch1[parent] = child
        # # ch1에 먼저 '자식'의 정보가 담겨있다면,
        # else: # ch1[parent] != 0:
        #     ch2[parent] = child
        elif ch2[parent] == 0: # 여기서 민준 튜터님은 else로 해도 된다고 하셨었는데, 그냥 elif를 지웠을 경우를 말씀하려던 것일까요????
            ch2[parent] = child
    # print(ch1)
    # print(ch2)
    # [0, 0, 0, 0, 0, 0, 0]
    # [0, 0, 0, 0, 0, 0, 0]

    count = 0
    descendant(N)

    print(f"#{i} {count}")