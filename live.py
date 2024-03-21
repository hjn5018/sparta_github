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
        list_.pop()

# str이 아닌 리스트를 쓰는 건 pop해야해서?
dfs()