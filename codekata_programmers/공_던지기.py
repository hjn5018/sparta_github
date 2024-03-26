def solution(numbers, k):
    if len(numbers) % 2 == 0:
        return numbers[2 * (k % (len(numbers) // 2)) - 1]
    else:
        if k*2 < len(numbers):
            return numbers[k*2 + 1]
        else:
            if (k*2 // len(numbers)) % 2 == 1:
                # 연산이.... 복잡해진다...