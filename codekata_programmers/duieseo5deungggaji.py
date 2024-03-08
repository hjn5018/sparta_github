# 정수로 이루어진 리스트 num_list가 주어집니다.
# num_list에서 가장 작은 5개의 수를 오름차순으로 담은 리스트를 return하도록 solution 함수를 완성해주세요.

# 6 ≤ num_list의 길이 ≤ 30
# 1 ≤ num_list의 원소 ≤ 100

# def solution(num_list):
#     sorted_list = sorted(num_list)
#     return sorted_list[:5]


num_list = [12, 4, 15, 46, 38, 1, 14]

num_list.sort()

print(num_list)

#.sort() 무서운 아이구나..