hex = '0123456789ABCDEF'
def ch(num, n):
    s = ''
    while num:
        num, s = num//n, hex[num%n] + s
    return s or '0'

def solution(n, t, m, p):
    s = ''
    num = 0
    while len(s) < t * m:
        s += ch(num, n)
        num += 1
    return s[p-1:t*m:m]