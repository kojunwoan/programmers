def solution(n):
    x, y = 0, 1
    for i in range(2, n + 1):
        x, y = y, x + y
    return y % 1234567