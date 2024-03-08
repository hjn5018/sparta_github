T = int(input())


for i in range(1, T+1):
    numbers = list(map(int, input().split()))
    sum = 0

    for num in numbers:
        sum += num

    avg = round(sum / 10) # 소수첫째에서 반올림 필요

    print(f"#{i} {avg}")