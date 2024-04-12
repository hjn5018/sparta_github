def solution(n):
    str_ = ''
    while n >= 3:
        quotient = n//3
        remainder = n - (n//3)*3
        str_ += str(remainder)
        n = quotient
    str_ += str(n)
    result = 0
    for i in range(len(str_)):
        result += int(str_[i]) * 3**(len(str_)-(i+1))
    return result