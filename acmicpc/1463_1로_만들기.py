def to_one(n):
    count = 0

    if n == 1:
        return count
    elif n % 3 == 0:
        count += 1
        return to_one(n // 3)
    elif n % 2 == 0:
        count += 1
        return to_one(n // 2)
    else:
        count += 1
        return to_one(n - 1)