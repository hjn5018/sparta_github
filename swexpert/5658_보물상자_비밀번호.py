import sys
from collections import deque
# sys.stdin = open('input.txt')

T = int(sys.stdin.readline())

for _ in range(1, T+1):
    N, K = map(int, sys.stdin.readline().split())

    hexadecial = sys.stdin.readline()
    # print(hexadecial)
    # 1B3B3B81F75E

    hexadecial = deque(hexadecial)
    # print(hexadecial)
    # deque(['1', 'B', '3', 'B', '3', 'B', '8', '1', 'F', '7', '5', 'E', '\n'])
    
    # split_hex = []
    # for _ in range(4):
        # split_hex.append(hexadecial[0 : N//4])
        # TypeError: sequence index must be integer, not 'slice'
        # hexadecial = hexadecial[N//4 : ]
        # print(split_hex)
        # print(hexadecial)
        # 1B3B3B81F75E
        # ['1B3']
        # B3B81F75E

        # ['1B3', 'B3B']
        # 81F75E

        # ['1B3', 'B3B', '81F']
        # 75E

        # ['1B3', 'B3B', '81F', '75E']
    



    # split_hex = []
    # for i in range(3):
        # split_hex.append(hexadecial[i])
        # print(split_hex)
        # ['1']
        # ['1', 'B']
        # ['1', 'B', '3']
    
    # split_hex = [[]*]