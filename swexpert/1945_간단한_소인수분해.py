# T = int(input())


# def factorization(n):
#     prime_list = [2, 3, 5, 7, 11]
#     count_list = [0, 0, 0, 0, 0]

#     if n == 1:
#         return " ".join(count_list)
#     else:
#         for i in range(len(prime_list)):
#             if n % prime_list[i] == 0:
#                 count_list[i] += 1
#                 return factorization(n//prime_list[i])


# for j in range(1, T+1):
#     N =int(input())

#     print(f"#{j} {factorization(N)}")

# null
# =================================================
T = int(input())


def factorization(n):
    prime_list = [2, 3, 5, 7, 11]
    count_list = [0, 0, 0, 0, 0]

    if n == 1:
        return " ".join(count_list)
    else:
        for i in range(len(prime_list)):
            if n % prime_list[i] == 0:
                count_list[i] += 1
                return factorization(n//prime_list[i])


for j in range(1, T+1):
    N =int(input())

    print(f"#{j} {factorization(N)}")
