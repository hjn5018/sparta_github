def geodeup(a, b):
    if b == 0:
        return 1
    else:
        result = a * geodeup(a, b - 1)
        return result

for i in range(1, 11):
    T = int(input())
    a, b = list(map(int, input().split()))
    answer = geodeup(a, b)
    print(f"#{i} {answer}")