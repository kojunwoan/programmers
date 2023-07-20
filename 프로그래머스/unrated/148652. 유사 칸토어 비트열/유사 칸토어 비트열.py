def ch(i):
    while i:
        if i % 5 == 2:
            return False
        i //= 5
    return True
    
def solution(n, l, r):
    return sum(map(ch, range(l - 1, r)))