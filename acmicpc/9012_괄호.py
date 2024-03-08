# 로직

# 받은 입력을 조사한다.
# 예시) "(())())"
# 이러한 입력을 test_case라고 하자.

# test_case가 VPS이기 위해서는 안 쪽 어딘가에는 "()"가 있어야한다.
# 맨 앞부터 순서대로 "()"와 일치하는 값을 찾는다.
# 편의상 가장 작은 VPS인 "()"를 basic_vps라고 한다.

# test_case의 앞부터 basic_vps를 찾는 순간, 해당 basic_vps를 지운다.
# 지우고나서 다시 test_case의 앞으로 돌아온다.
# 위 두 과정을 반복한다.

# 반복하고 남은 값이 있는 경우 "NO"를 반환한다.
# 예시) "))"

# 반복하고 남은 값이 없는 경우 "YES"를 반환한다.
# -> 모두 VPS로 이루어져 있었다는 결론입니다!


T = int(input())

# 1. 사전에 ()에 대해 정의한다.
basic_vps = "()"

# 스켈레톤 코드
for i in range(1, T+1): # T개의 테스트 케이스를 받습니다.
    test_case = input() # 입력을 받고, test_case라고 이름 붙입니다.

    for j in test_case: # test_case 내부의 각 원소에 대해 조사합니다.
        result = is_vps(test_case) # 이 때 is_vps 함수는 해당 원소가 vps인지 검사하고,
                                   #  YES 또는 NO를 반환합니다.
        return result # 결과로 받은 YES 또는 NO를 반환합니다.

# =================================================================
# is_vps 스켈레톤 코드
# 1``
# 1. 틸출부터 만들어본다.
# 2. else에서 무언가를 처리하고, 재귀한다.
def is_vps(a):
    if a == 0: 
        return 0 # 이 떄 리턴은 ??
    else:
        is_vps(a) = b + is_vps(a-1) # 처리하는 일 : basic_vps를 제거한다. a-1은 basic_vps를 없앤 str이 들어가야한다.
# ==============================================
stack = []

brackets = {'[':']', '{':'}', '(':')'}

stack.push(test_case[0])
stack.push(test_case[1])

(예린 튜터님 -> push가 아닌 append를 쓰세요~)