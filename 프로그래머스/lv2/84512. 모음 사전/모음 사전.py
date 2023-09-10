from itertools import product
def solution1(word):
    return sorted("".join(p) for n in range(5) for p in product('AEIOU', repeat=n+1)).index(word) + 1


def solution(word):
    global cnt
    cnt = 0
    
    def dps(sub):
        global cnt
        if sub == word:
            return cnt
        elif len(sub) == 5:
            return 0
        for al in 'AEIOU':
            cnt += 1
            if dps(sub + al):
                return cnt

    return dps("")