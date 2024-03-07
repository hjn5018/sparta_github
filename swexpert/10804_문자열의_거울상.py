T = int(input())
for i in range(1, T+1):
    case = input()
    case = case[::-1]
    #b->d, d->b
    #p->q, q->p로 바꾸는 작업이 필요.
    case.replace('b','d')
    case.replace('p','q') # 여기까진 괜찮은데
    case.replace('d','b') # 여기부터는 이미 바꾼걸 다시 바꿔서 오셀로마냥 다 b가 되어버릴 수 있다....... replace를 자세히 볼까
    case.replace('q','p') # replace에 뭐 특별한 기능같은건 없다..

    #  replace를 적용하는 순간 흐트러진다.
# ==================================================
    # 사전상 b 가 d에 앞선다.
    # 사전상 p 가 q에 앞선다.
    # 정렬을 한다면..?
    # 이건 아닌 것 같다..........
# ===================================================
# 격하게 아래로 뒤집고 싶다...

# 거울 함수가 있을리 만무하고
# 뒤집는 것도 그렇고

# 대체핢 만한 게 있긴 한가..

# for 문으로 소환하고 같은 로직으로 돌려야하니까 manually는 안되고

def baggwer(str_):
    if 'b' in str_ and 'q' in str_:
        # change their position
        # 1. search their position
        # 2. crose their position
        
        # 1.
        for i in str_:
            # ???????????????????????
# =========================================================
def baggwer(str_):
    if 'b' in str_ and 'q' in str_:
        # change their position
        # 1. search their position
        # 2. crose their position
        
        # 1.
        for i, j in enumerate(str_):
            # 이건 규모가 너무 커지는데..................
# ===============================================================
# 사전에 copy를 따놓고
# 일단 replace를 해서
# copy본과 replace본을 비교하고
# 같은 거는 다르도록 replace로 바꾼다
# ex)
# bd -> copy bd
#    -> replace bb

# copy bd와 replace bb를 비교

# 겹치는 0번째의 b를 d로 replace

# replace bb-> rereplace db

# 되려나??
# 이건 케이스의 길이//조합에 따라 안되는 경우가 허다하다..
# ===============================================
동현님
거울 dictionay 짜고, reversed()사용
