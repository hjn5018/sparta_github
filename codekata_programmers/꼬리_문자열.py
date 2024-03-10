def solution(str_list, ex):
    answer = ''
    for str_ in str_list:
        if ex not in str_:
            answer += str_
    return answer