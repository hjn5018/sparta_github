def solution(arr):
    str_ = ''
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == arr[j][i]:
                str_ += '1'    
            else:
                str_ += '0'
    if '0' in str_:
        return 0
    else:
        return 1