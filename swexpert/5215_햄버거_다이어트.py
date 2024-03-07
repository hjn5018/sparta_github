T = int(input())
N, L = list(map(int, input().split()))

# for i, j in enumerate(range(1, N+1), 1):
for i in range(N):
    i_T, K = list(map(int, input().split())) # i번째 T라는 걸 나타내기 까다로운데... T_i 하면 range가 알아듣나..?
# ============================================================
T = int(input())
N, L = list(map(int, input().split()))

for i in range(N):
    M, K = list(map(int, input().split()))
    # 모든 조합의 경우의 수는 ?
    # 1개 -> 5
    # 2개 -> 5*4/2
    # 3개 -> 5*4/2
    # 4개 -<> 5
    # 5개 ->1
    
    # 다 돌아보고
    # 칼로리가 1000 이하인 걸 골라내고
    # 맛 점수 높은 걸 고른다...
    #시간이 좀 걸릴 것 같은데..
    
    # 일단 다 돌아볼 때 맛점수, 칼로리를 뱉어내게 해야한다.
    # 그렇다면 조합을 어떻게 짜야하나..
    
    # 그 전에 네이밍//인덱싱 부터 해야겠는데..
# ====================================================================
    # 그냥 애초부터 1000넘지 않는 조합을 찾고
    # 거기서 최대를 찾으면 될 듯?
    
    # 일단 네이밍을 해야 수월할 것 같은데..
# ===========================================================
T = int(input())
N, L = list(map(int, input().split()))

#for i in range(N):
#    M, K = list(map(int, input().split()))
M1, K1 = list(map(int, input().split()))
M2, K2 = list(map(int, input().split()))
M3, K3 = list(map(int, input().split()))
M4, K4 = list(map(int, input().split()))
M5, K5 = list(map(int, input().split()))

# 이렇게 할까....
# =========================================================

# 300 500
# 250 300
# 500 1000
# 400 400


# for i in range(4):
#     M, K = list(map(int, input().split()))
# print(M, K)
# 400 400
# =========================================
# for i in range(4):
#     M_i, K_i = list(map(int, input().split()))
# print(M_i, K_i)
# ???
# ============================================
# for i, j in enumerate(range(4), 1):
#     M, K = list(map(int, input().split()))
# print(M, K)
# 400 400

# print(i, j)
# 4, 3
# 오호라..
# 이러면 enumerate를 range()로 돌리는 게 아니라
# M들의 리스트/K들의 리스트로 돌면 될 것 같은데?
# 그걸 어떻게 하지...........
# ==============================================
for i in enumerate(range(4)):
    M_K_list = list(map(int, input().split()))
    
    for j, k in enumerate(M_K_list, 1):
        print(j, k)
# 300 500
# 1 300
# 2 500
# 250 300
# 1 250
# 2 300
# 500 1000
# 1 500
# 2 1000
# 400 400
# 1 400
# 2 400

# 내가 원한 건 이 순서가 아닌데...