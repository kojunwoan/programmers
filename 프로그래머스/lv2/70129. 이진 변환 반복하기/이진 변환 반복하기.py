def solution(s):
    c, z = 0, 0
    while s != '1':
        c += 1
        z += s.count('0')
        s = f"{s.count('1'):b}"
    return [c, z]