T = int(input())

for i in range(1, T+1):
    a, b = map(int, input().split())

    print(f"#{i} {a // b} {a % b}")

# 3
# 9 2
# 15 6
# 369 15