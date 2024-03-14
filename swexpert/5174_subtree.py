import sys

T = int(sys.stdin.readline())

for _ in range(1, T+1):
    E, N = map(int, sys.stdin.readline().split())
    pair_list = list(map(int, sys.stdin.readline().split()))

    keys = []
    values = []
    for i in range(len(pair_list)):
        if i % 2 == 0:
            keys.append(pair_list[i])
        else:
            values.append(pair_list[i])
    # print(keys)
    # print(values)
    # [2, 2, 1, 5, 6]
    # [1, 5, 6, 3, 4]

    # pair_dict = {}
    # for i in range(len(keys)):
    #     pair_dict[keys[i]] = values[i]
    # print(pair_dict)
    # {2: 5, 1: 6, 5: 3, 6: 4}
    
    
