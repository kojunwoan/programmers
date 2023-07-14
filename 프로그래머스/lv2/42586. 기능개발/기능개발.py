def solution(progresses, speeds):
    last, res = 0, []
    for p, s in zip(progresses, speeds):
        date = -((p - 100) // s)
        if date > last:
            last = date
            res.append(1)
        else:
            res[-1] += 1
            
    return res