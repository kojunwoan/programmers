from heapq import heappush, heappop, heapify
def solution(scoville, K):
    heapify(scoville)
    start = len(scoville)
    while scoville[0] < K:
        if len(scoville) < 2:
            return -1
        else:
            heappush(scoville, heappop(scoville) + 2*heappop(scoville))
    return start - len(scoville)