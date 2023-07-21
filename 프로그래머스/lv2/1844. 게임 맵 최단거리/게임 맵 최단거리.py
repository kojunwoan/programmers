def solution(maps):
    X, Y = len(maps[0]) - 1, len(maps) - 1
    loads = {(x, y) for y, m in enumerate(maps) for x, v in enumerate(m) if v}
    queue = [(1, (0, 0))]
    loads.remove((0, 0))
    while queue:
        c, (x, y) = queue.pop(0)
        if (x, y) == (X, Y):
            return c
        for nx, ny in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
            npos = (x + nx, y + ny)
            if npos in loads:
                queue.append((c + 1, npos))
                loads.remove(npos)
    return -1