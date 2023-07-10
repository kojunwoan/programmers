from collections import defaultdict
def solution(clothes):
    col = 1
    clothes_d = defaultdict(list)
    for cloth in clothes:
        clothes_d[cloth[1]].append(cloth[0])
    for cloth in clothes_d.values():
        col *= len(cloth) + 1
    return col - 1