def solution(hp):
    # result = a+b+c
    # 5a + 3b + 1c = hp
    # return result
    
    # a부터 촤르륵
    # hp % 5 => 5_hp = hp % 5
"""
    5_hp = hp % 5
    3_hp = 5_hp % 3 
    # -> c
    c = 3_hp
    a = hp // 5
    b = hp // 3
    
    return a+b+c
"""
#     5_hp = hp % 5
#      ^
# SyntaxError: invalid decimal literal
# ==========================================
#     hp_p5 = hp % 5
#     hp_p3 = hp_p5 % 3 

#     c = hp_p3
#     a = hp // 5
#     b = hp // 3
    
#     return a+b+c
# 실행한 결괏값 11이 기댓값 5과 다릅니다.
# ========================================

def solution(hp):
#     hp // 5 => a
#     (hp % 5) // 3 => b
#     ((hp % 5) % 3) => c
    
    a = hp // 5
    b = (hp % 5) // 3
    c = ((hp % 5) % 3)
    
    return a+b+c
# 내 정답
# =======================================
def solution(hp):
    answer = 0
    for ant in [5, 3, 1]:
        d, hp = divmod(hp, ant)
        answer += d
    return answer
# 다른 사람 풀이
# 김현우 , JamesPsh , 김민우 , Kim Jin Woo 외 38 명

# divmod(num1,num2) # num1을 num2 로 나눈 몫과 나머지를 출력하는 함수 박기현―2022.11.11 10:19
# =========================================
def solution(hp):
    count = 0
    ants = [5, 3, 1]    

    for att in ants:
        count += hp // att
        hp %= att

    return count
# tool5047@gmail.com의 풀이