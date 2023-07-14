def solution(numbers, target):
    res = [0]
    for num in numbers:
        res = [r + s*num for r in res for s in (1, -1)]
    return res.count(target)