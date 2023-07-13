def solution(money):
    first = money[:-1]
    last = money[1:]
    firstmax = {-1 : 0, 0 : first[0], 1 : first[1]}
    lastmax = {-1 : 0, 0 : last[0], 1 : last[1]}
    for i in range(2, len(first)):
        firstmax[i] = max(firstmax[i-3] + first[i], firstmax[i-2] + first[i])
        lastmax[i] = max(lastmax[i-3] + last[i], lastmax[i-2] + last[i])
    return max(list(firstmax.values())[-2:] + list(lastmax.values())[-2:])