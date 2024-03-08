# x 좌표 (x, y)를 차례대로 담은 정수 배열 dot이 매개변수로 주어집니다.
# 좌표 dot이 사분면 중 어디에 속하는지 1, 2, 3, 4 중 하나를 return 하도록 solution 함수를 완성해주세요.

# dot의 길이 = 2
# dot[0]은 x좌표를, dot[1]은 y좌표를 나타냅니다
# -500 ≤ dot의 원소 ≤ 500
# dot의 원소는 0이 아닙니다.

def solution(dot):
    if dot[0] > 0 and dot[1] > 0:
        return 1
    elif dot[0] < 0 and dot[1] > 0:
        return 2
    elif dot[0] < 0 and dot[1] < 0:
        return 3
    elif dot[0] > 0 and dot[1] < 0:
        return 4

# dot = [3,1]
# # 1
# dot = [-3,1]
# # 2
# dot = [-3,-3]
# # 3
# dot = [3,-3]
# # 4
    
# result = solution(dot)

# print(result)