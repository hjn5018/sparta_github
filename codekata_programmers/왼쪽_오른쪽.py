def solution(str_list):
    for i in range(len(str_list)):
        if str_list[i] == 'l':
            if i == 0:
                return [] # l이 오른쪽 끝에!
            return str_list[:i] # 왼쪽 리스트 
            
        if str_list[i] == 'r':
            if i == len(str_list):
                return [] # r이 오른쪽 끝에!
            return str_list[i+1:] # 오른쪽 리스트
    return [] # ud밖에 없어!