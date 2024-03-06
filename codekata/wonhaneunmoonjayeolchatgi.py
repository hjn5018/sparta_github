# 알파벳으로 이루어진 문자열 myString과 pat이 주어집니다. myString의 연속된 부분 문자열 중 pat이 존재하면 1을 그렇지 않으면 0을 return 하는 solution 함수를 완성해 주세요.

# 단, 알파벳 대문자와 소문자는 구분하지 않습니다.

# 1 ≤ myString의 길이 ≤ 100,000
# 1 ≤ pat의 길이 ≤ 300
# myString과 pat은 모두 알파벳으로 이루어진 문자열입니다.

def solution(myString, pat):
    if pat.lower() in myString.lower():
        return 1
    else:
        return 0

# 대소문자 구분하지 않는다는게.............
# 파이썬은 원래 구분하지만, 관용을 베푼다.. 뭐 그런 것 같다...