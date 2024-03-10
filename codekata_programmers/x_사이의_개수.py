def solution(myString):
    answer = []
    split_myString = myString.split("x")
    for string in split_myString:
        answer.append(len(string))
    return answer

# # myString = "oxooxoxxox"
# # result = [1, 2, 1, 0, 1, 0]
# # [1, 2, 1, 0, 1, 0]

# myString = "xabcxdefxghi"
# # result = [0, 3, 3, 3]
# # [0, 3, 3, 3]

# result = solution(myString)

# print(result)
# ==========================================================
# myString = "oxooxoxxox"
# ['o', 'oo', 'o', '', 'o', '']
# myString = "xabcxdefxghi"
# ['', 'abc', 'def', 'ghi']


# split_myString = myString.split("x")

# print(split_myString)
# =============================================
# split 요소 사이에 아무것도 없으면 비어있는 스트링,
# split 요소가 맨 앞 // 맨 뒤에 있으면 비어있는 스트링을 반환한다.