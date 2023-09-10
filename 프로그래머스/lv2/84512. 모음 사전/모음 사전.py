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