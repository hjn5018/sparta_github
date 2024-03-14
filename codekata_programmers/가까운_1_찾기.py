def solution(arr, idx) :
    for i, v in enumerate(arr) :
        if v==1 and i>=idx :
            return i
    return -1
    # for문을 다 돌고 -1 return한다.
# =================================
def solution(arr, idx) :
    for i, v in enumerate(arr) :
        if v==1 and i>=idx :
            return i
        else:
            return -1
        # 첫 번째 인덱스에서 바로 i냐 -1가 결정된다.
# ==============================
def solution(arr, idx) :
    for i, v in enumerate(arr) :
        if v==1 and i>=idx :
            break
            
    else:
        return -1
    return i
    
    # for를 다 돌고 else를 쓰면.. 허공에 else를 쓰는 것인가..?
    # for else 구문임.
# ===============================
def solution(arr,idx) :
    for i in range(len(arr)):
        if arr[i] == 1 and i >= idx:
            return i
    return -1