def solution(n, a, b):
    a, b = a - 1 , b - 1
    c = 0
    while a != b:
        a >>= 1
        b >>= 1
        c += 1
    return c