from collections import deque
def match(c):
    stack = []
    while c:
        p = c.popleft()
        i = ')]}'.find(p)
        if i != -1:
            if not stack or stack[-1] != '([{'[i]:
                stack.append(p)
                break
            else:
                stack.pop()
        else:
            stack.append(p)
    return not c and not stack

def solution(s):
    result = 0
    s = deque(s)
    for _ in range(len(s)):
        s.rotate(-1)
        result += match(deque(s))
    return result