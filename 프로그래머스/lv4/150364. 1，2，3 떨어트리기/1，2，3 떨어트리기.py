from collections import defaultdict
def solution(edges, target):
    edges_d = defaultdict(list)
    for e in edges:
        edges_d[e[0]].append(e[1])
    for k in edges_d:
        edges_d[k].sort()
    
    target_g = [{"min": -(-n//3), "max": n} for n in target]
    target_c = [0 for _ in target]
    
    track = []
    while True:
        node = 1
        while node in edges_d:
            edges_d[node], node = edges_d[node][1:] + edges_d[node][:1], edges_d[node][0] 
        track.append(node)
        target_c[node - 1] += 1
        for g, c in zip(target_g, target_c):
            if g["min"] > c:
                break
            if g["max"] < c:
                return [-1]
        else:
            break

    target_n = []
    for t, c in zip(target, target_c):
        if t:
            n3, n2 = divmod(t - c, 2)
            c = [3]*n3 + [2]*n2 + [1]*(c-n3-n2)
        target_n.append(c)
    return [target_n[t-1].pop() for t in track]