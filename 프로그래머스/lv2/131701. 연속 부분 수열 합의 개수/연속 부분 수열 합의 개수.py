def solution(elements):
    le = len(elements)
    res = set()
    for i in range(le):
        s = 0
        for j in range(le):
            s += elements[(i+j)%le]
            res.add(s)
    return len(res)