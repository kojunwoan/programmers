from math import gcd
def solution(arr):
    lcm = arr.pop()
    for a in arr:
        lcm = lcm * a // gcd(lcm, a)
    return lcm