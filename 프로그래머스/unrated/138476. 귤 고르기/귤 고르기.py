from collections import Counter
def solution(k, tangerine):
    answer = 0
    c = Counter(tangerine)
    for i, (_, m) in enumerate(c.most_common()):
        answer += m
        if answer >= k:
            return i + 1