def ch(i):
    i -= 1
    while i:
        i, m = divmod(i, 5)
        if m == 2:
            return False
    return True
    
def solution(n, l, r):
    return sum(map(ch, range(l, r + 1)))