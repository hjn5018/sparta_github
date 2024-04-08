def solution(n, m):
    list_ = []
    for i in range(1, m+1):
        if m % i == 0:
            list_.append(i)
    
    list_A = []
    for i in range(1, n+1):
        if n % i == 0:
            list_A.append(i)
    
    list_B = []
    for i in list_:
        if i in list_A:
            list_B.append(i)
    
    lcm = max(list_B)
    gcd = lcm * (n / lcm) * (m / lcm)
    
    return lcm, gcd