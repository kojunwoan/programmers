def solution(brown, yellow):
    for i in range(1, yellow + 1):
        if yellow/i + 2 == (brown + yellow)/(i + 2):
            return [yellow/i + 2, i + 2]