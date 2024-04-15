def solution(s):
    count = 0
    str_ = ''
    for i in s:
        if i.isalpha():
            if count % 2 == 0:
                str_ += i.upper()
            else:
                str_ += i.lower()
            count += 1
        else:
            str_ += i
            count = 0
    return str_
                