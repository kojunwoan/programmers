def solution(want, number, discount):
    res = 0
    for i in range(len(discount)):
        if discount[i] in want:
            number[want.index(discount[i])] -= 1
        if i >= 10:
            if discount[i-10] in want:
                number[want.index(discount[i-10])] += 1
        
        if not any(number):
            res += 1
    return res