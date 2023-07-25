from heapq import heappush, heappop, heapify
def solution(operations):
    max_h, min_h, cnt = [], [], 0
    for oper in operations:
        op, num = oper.split()
        if op == 'I':
            heappush(min_h, int(num))
            heappush(max_h, -int(num))
            cnt += 1
        if op == 'D' and cnt:
            f, t = (max_h, min_h) if num == '1' else (min_h, max_h)
            t.pop(t.index(-heappop(f)))
            heapify(t)
            cnt -= 1
    return [-max_h[0], min_h[0]] if cnt else [0, 0]