from heapq import heappush, heappop
def solution1(n, s, a, b, fares):
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

def solution(n, s, a, b, fares):
    d = [ [ 20000001 for _ in range(n) ] for _ in range(n) ]
    for x in range(n):
        d[x][x] = 0
    for x, y, c in fares:
        d[x-1][y-1] = c
        d[y-1][x-1] = c

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if d[j][k] > d[j][i] + d[i][k]:
                    d[j][k] = d[j][i] + d[i][k]

    minv = 40000002
    for i in range(n):
        minv = min(minv, d[s-1][i]+d[i][a-1]+d[i][b-1])
    return minv