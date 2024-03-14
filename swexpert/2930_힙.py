import sys

# sys.stdin = open('input.txt')

T = int(sys.stdin.readline())

for i in range(1, T+1):
    N = int(sys.stdin.readline())

    list_ = []
    answer = [] # 출력의 대답 모아두기
    for _ in range(N):
        operation = list(map(int, sys.stdin.readline().split()))
        if operation[0] == 1:
            pass
            list_.append(operation[1])
        else: # 2 연산이 온 경우
            if list_ == []: # popleft? 해야하는데 리스트가 비어있을 경우
                answer.append('-1')
            else:
                answer.append(list_[0])
                list_.remove(0)
                # 그리고 순서 당기기
                
