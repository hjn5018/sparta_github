# N, M = map(int, input().split())

# # 1 ~ N의 자연수 중 M개를 뽑아 나열한다.
# # 개수를 구하는 게 아니고, 진짜 나열한다.

# # 일단 뽑는다.
# # 작은 합부터 나열한다.

# # 일단 1~N을 리스트에 둔다.
# list_ = []

# for i in range(1, N+1):
#     list_.append(i)*M #뭐 대충 이런 개념

# # list_[:M] # M개까지 자른다????????
# # ㄴㄴ

# # M개를 골라야한다.

# # combination??? import????
    
# # 1찍고 투다다다
# # 2찍고 투다다다
# # 3찍고 투다다다
# # M만큼 for를 넣어야....??????????
    
# # 재귀............?
# # ============================================
# # for i in range(1, N+1):

# N = 7
# M = 4 라고 해보자

# 1 2 3 4
# ...
# 1 5 6 7
# 2 1 3 4
# ...
# 4 5 6 7


# 1고정하면 n-1, m-1 인 경우 투다다다
# 이걸 n번 반복

# 7중 1 뺐고
# (
# 6중 3 돌려야하고
# 5중 2 돌려야하고
# 4중 1 돌려야한다.
# )
# 이걸 7번 한다.
# def jaegui(N, M):
#     if M == 1:


# # =================================================

# 1. 하나의 숫자를 고른다.(시작숫자)
# 2. 그 상태에서 다른 숫자를 고른다.
#     a. (2)를 n-1번 반복한다.
#     b. 만약, 내가 고른 숫~~

# # ==============================================

# N, M = map(int, input().split())

# while True:#??:

#     print()

# for i in range(N):
    # print(i, end="") print(i+1)
    # for j in range(i+1, N-1):
        # 1,1 X
    # L = L[]
    # for j in range()

# picked_list = [] # 1번 방법 : dfs 넘어갈 때마다 쌓고 pop // visited??

# def dfs():
#     if len(picked_list) == M: 
#         print(picked_list)
#         return 

#     for i in range(1, N+1):
#         if i in picked_list:
#             continue    
#         picked_list.append(i)
#         dfs()
#         picked_list.pop()


# dfs()



# # 8 5
# 12345

# 45678
# ================================
# N, M = map(int, input().split())

# list_ = []
# def dfs():
#     if len(list_) == M:
#         print(f'{" ".join(map(str, list_))}')
#         # SyntaxError: f-string: expecting '}'
#         # result = " ".join(map(str, list_))
#         # print(result)
#         return
    
#     for i in range(1, N+1):
#         if i in list_:
#             continue
#         list_.append(i)
#         dfs()
#         list_.pop()

# dfs()
# ===========================================
# N, M = map(int, input().split())

# list_ = []
# def dfs():
#     if len(list_) == M and sorted(list_) == list_:
#         result = " ".join(map(str, list_))
#         print(result)
#         return
    
#     for i in range(1, N+1):
#         if i in list_ or i <= max(list_) if list_ else 0:
#             continue
#         list_.append(i)
#         dfs()
#         list_.pop()

#         # try except...

#         # if i > max(list_):
#         #     ValueError: max() arg is an empty sequence
#         #     list_.append(i)
#         #     dfs()
#         #     list_.pop()

#         # if i > list_[len(list_)]:
#             # IndexError: list index out of range
#             # list_.append(i)
#             # dfs()
#             # list_.pop()

# dfs()
# ===================================================
N, M = map(int, input().split())


def dfs(picked_list: list[int]) -> None:
    if len(picked_list) == M: 
        print(' '.join(picked_list))
        return 

    
    for i in range(1, N+1):
        if i in picked_list:
            continue
        dfs(picked_list=picked_list+[i])
        # dfs(picked_list+=[i])
        # SyntaxError: invalid syntax
# print(1 + 0)
# print(1)
# picked_list=picked_list+[i]
dfs('')
# ===================================
N, M = map(int, input().split())

# 1,2 심어놓고 투다다 -> dfs
list_ = []
def dfs():
    if len(list_) == M:
        print(list_)
        return
    
    # 첫 번째 수가 N까지 돌긴해야하니까 for문
    for i in range(1, N+1):
        if i in list_:
            continue
        list_.append(i)
        dfs()
        # list_.pop()
        []

# str이 아닌 리스트를 쓰는 건 pop해야해서?
dfs()
# =====================================
N, M = map(int, input().split())

num_list = list(map(int, input().split()))
num_list.sort()
list_ = []
def dfs():
    if len(list_) == M:
        print(list_)
        return
    
    for i in num_list:
        # if i in list_:
        #     continue
        list_.append(i)
        dfs()
        list_.pop()

dfs()
























''.join(map(filter)(str, iter_))

# ===================





























n
L = [1,2,3,4,5]

L2 = L[:1] + L[1+1:] - >O(n)



N, M = map(int, input().split())


def dfs():
    if



    # 구조
    for
        dfs()
