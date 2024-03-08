def solution(my_strings, parts):
    str_ = ''
    for i in range(len(parts)):
        parts[i] = [int(parts[i][0]):int(parts[i][1])+1]
        str_.append(my_string[i]parts[i])
    return str_

#     parts[i] = [int(parts[i][0]):int(parts[i][1])+1]
#                                 ^
# SyntaxError: invalid syntax
# =========================================================
def solution(my_strings, parts):
    str_ = ''
    # 스트링에 이어붙인다.
    # 돌면서 여기서는 이거
    # 저기서는 저거
    
    # 1.인덱싱해서 붙이고
    # 2. 그러려면 parts를 바꿔야하는데..
    # 3. end를 바꿔야한다.
    for i in range(len(parts)):
        # parts[i] # i번째 리스트
        # 그대로 가져와서 슬라이싱에 쓸 수는 없구낭..
        # s, e = parts[i] 로 가져오면 쓸 수 있나?
        s, e = parts[i]
        # my_string[s : e+1]하면 ???
        # str_.append(my_string[s : e+1]) 어펜드가 아니라 +=지..
        str_ += my_strings[s : e+1]
    return str_
    # TypeError: can only concatenate str (not "list") to str
# ============================================================
def solution(my_strings, parts):
    str_ = ''

    for i in range(len(parts)):
        s, e = parts[i]
        str_ += my_strings[i][s : e+1]
    return str_

# i번째를 꺼내지 않았구나...
# my_strings = ["progressive", "hamburger", "hammer", "ahocorasick"]
# parts = [[0, 4], [1, 2], [3, 5], [7, 7]]
# result = "programmers"