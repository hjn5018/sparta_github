# 입력
# 10
# 3
# 1 2 3
# 4 5 6
# 7 8 9
        
# 출력
# #1
# 741 987 369
# 852 654 258
# 963 321 147
# ============================
T = int(input())

for i in range(len(1,T+1)):
    N = int(input())

    for j in range(len(N)):
        test_case = list(map(int, input().split()))
    
# 일단 123을 받았는데.. 이걸 출력하려면 세로로 뿌려야하고..
# 세로로 뿌리려면 ??? for 문으로 뿌려야겠는데
# print()에는 뭐라고 할거임..?

# 그럼 다시
# 테스트케이스를 다 받는다 치면..
# 마지막 테스트케이스만 남아버린다..
# 이걸 휘발되지 않게 하려면??
# 리스트로 받았지만 리스트에 넣어야할 것 같은데???

# 그러면.. 각각을 변수에 넣어야하나??
# a, b, c = list(map(int, input().split()))
# 이러면 길이가 N이니까 N개의 변수를 만들어줘야해서 좀...

# 그러면 어떻게 리스트에 넣어야하나..
# =============================
# T = int(input())

# for i in range(len(1,T+1)):
#     N = int(input())

#     for j in range(len(N)):
#         test_case = list(map(int, input().split()))

#         for k in range(len(N)):
#             test_case[i]
# for를 3번이나??? 이건 좀;;;;;;;;;;

