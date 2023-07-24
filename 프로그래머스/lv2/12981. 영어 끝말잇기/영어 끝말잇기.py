from itertools import cycle
def solution(n, words):
    peo = {i: [] for i in range(1, n+1)}
    word_set = set()
    last = None
    for w, p in zip(words, cycle(range(1, n+1))):
        peo[p].append(w)
        if (last and last != w[0]) or w in word_set:
            return [p, len(peo[p])] 
        else:
            word_set.add(w)
        last = w[-1]
    return [0, 0]