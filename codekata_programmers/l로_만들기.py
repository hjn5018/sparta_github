# def solution(myString):
#     for i in range(len(myString)):
#         if ord(myString[i]) < ord('l'):
#             myString[i] = 'l'
#             # TypeError: 'str' object does not support item assignment
            
#     answer = myString
#     return answer
# ==============================================
def solution(myString):
    for i in range(len(myString)):
        if ord(myString[i]) < ord('l'):
            # myString[i].replace('l')
            # TypeError: replace expected at least 2 arguments, got 1
            myString = myString.replace(myString[i], 'l')

    answer = myString
    return answer

myString = "abcdevwxyz"

print(solution(myString))