from collections import deque
def solution(people, limit):
    p_que = deque(sorted(people))
    count = 0
    while p_que:
        max = p_que.pop()
        try:
            min = p_que.popleft()
        except:
            min = 0
        if max + min > limit:
            p_que.appendleft(min)
        count += 1
    return count