from collections import deque
def solution(priorities, location):
    que = deque(enumerate(priorities))
    for c in range(len(que)):
        que.rotate(-que.index(max(que, key=lambda x: x[1])))
        if location == que.popleft()[0]:
            return c + 1