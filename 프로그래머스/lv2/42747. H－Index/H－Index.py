def solution(citations):
    citations.sort(reverse=True)
    h, t = 0, len(citations)
    for c in citations:
        while t > c:
            t -= 1
            if h == t:
                return h
        h += 1
        if h == t:
            return h