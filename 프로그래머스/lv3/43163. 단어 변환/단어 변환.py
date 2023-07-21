import re
def solution(begin, target, words):
    queue = list()
    visited = set()
    
    def find(n, begin):
        for i in range(len(begin)):
            t = ""
            for j in range(len(begin)):
                if i == j:
                    t += "."
                else:
                    t += begin[j]

            for w in words:
                if re.match(t, w) and w not in visited:
                    queue.append((n + 1, w))
                    visited.add(w)
    
    find(0, begin)
    while queue:
        n, begin = queue.pop(0)
        if begin == target:
            return n
        find(n, begin)
    
    return 0