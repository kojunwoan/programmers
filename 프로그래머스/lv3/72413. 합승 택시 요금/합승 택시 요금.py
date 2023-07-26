from heapq import heappush, heappop
def solution(n, s, a, b, fares):
    path = {}
    for n1, n2, c in fares:
        path.setdefault(n1, {n1: 0})[n2] = c
        path.setdefault(n2, {n2: 0})[n1] = c
    
    costs = []
    for no in [s, a, b]:
        que = [(0, no)]
        cost = {}
        while que:
            s_c, l = heappop(que)
            for p, c in path[l].items():
                sum_c = s_c + c
                if (p not in cost) or (cost[p] > sum_c):
                    cost[p] = sum_c
                    heappush(que, (sum_c, p))
        costs.append(cost)
    
    return min(sum(map(lambda d: d[i], costs)) for i in costs[0])