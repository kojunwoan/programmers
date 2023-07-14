
def solution(n):
    left = n + (-n & n)
    right = (n ^ left) // (-n & n) >> 2
    return left + right