def solution(n, s):
    base, cnt = divmod(s, n)
    if not base:
        return [-1]
    return [base + (i >= n - cnt) for i in range(n)]