from math import ceil
from collections import deque
def solution(progresses, speeds):
    last, res = 0, []
    for p, s in zip(progresses, speeds):
        date = ceil((100 - p) / s)
        if date > last:
            last = date
            res.append(1)
        else:
            res[-1] += 1
            
    return res