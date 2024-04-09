def solution(s):
#     str_ = ''
#     for i in s:
#         str_ += i
#         if '()'in str_:
#             str_ = str_[0:len(str_)-2]
    
#     if str_:
#         return False
#     return True
#     # 시간 초과
    list_ = []
    idx = -1
    for i in range(len(s)):
        list_ += s[i]
        if s[i] == ')' and list_[idx] == '(' and i > 0:
            list_.pop()
            list_.pop()
            idx -= 2
        idx += 1
    if list_:
        return False
    return True