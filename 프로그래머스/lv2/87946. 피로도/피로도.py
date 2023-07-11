from itertools import permutations
def solution(k, dungeons):
    max = 0
    for case in permutations(dungeons, len(dungeons)):
        r_k, now = k, 0
        for lea, con in case:
            if r_k >= lea:
                r_k -= con
                now += 1
            else:
                if max < now:
                    max = now
                break
        else:
             return now
    return max