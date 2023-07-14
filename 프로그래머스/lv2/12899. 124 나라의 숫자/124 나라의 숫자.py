def solution(n):
    s = ""
    while n:
        n, m = divmod(n - 1, 3)
        s = "124"[m] + s
    return s