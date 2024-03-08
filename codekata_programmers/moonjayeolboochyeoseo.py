# 두 개의 문자열 str1, str2가 공백으로 구분되어 입력으로 주어집니다.
# 입출력 예와 같이 str1과 str2을 이어서 출력하는 코드를 작성해 보세요.

# 1 ≤ str1, str2의 길이 ≤ 10

str1, str2 = input().strip().split(' ')


# input
# 아니야 그래
# --> strip으로 앞뒤 공백 자르고, 중앙 공백은 split이 자른다.
# print(str1)
# 아니야
# print(str2)
# 그래

print(str1 + str2)

# ==========strip method===============================================
# strip method는 앞뒤 공백을 자른다.
# 인자로 char를 받을 수 있는데, 따옴표에 감싸진 채로 받는다.
# 밖에서부터 해당 char를 지우다가 멀쩡한 거 만나면 멈춘다.

# comment_string = '#....... Section 3.2.1 Issue #32 .......'
# comment_string.strip('.#! ')
# 'Section 3.2.1 Issue #32'

# 'www.example.com'.strip('cmowz.')
# 'example'
# ==================================================================