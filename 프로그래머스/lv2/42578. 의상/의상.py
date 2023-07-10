from collections import defaultdict
def solution(clothes):
    col = 1
    clothes_d = defaultdict(list)
    for cloth, kind in clothes:
        clothes_d[kind].append(cloth)
    for cloth in clothes_d.values():
        col *= len(cloth) + 1
    return col - 1