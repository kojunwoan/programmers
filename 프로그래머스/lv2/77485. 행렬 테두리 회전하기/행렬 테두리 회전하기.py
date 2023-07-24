def solution(rows, columns, queries):
    result = []
    Array = [[r * columns + c + 1 for c in range(columns)] for r in range(rows)]
    for y1, x1, y2, x2 in queries:
        Y, X = y1 -1, x1 - 1
        tmp = []
        for (x, y), cnt in zip(((1,0),(0,1),(-1,0),(0,-1)), [x2-x1, y2-y1]*2):
            for i in range(cnt):
                tmp.append(Array[Y][X])
                Y, X = Y + y, X + x
        result.append(min(tmp))
        hashmap = dict(zip(tmp, tmp[-1:] + tmp[:-1]))
        for (x, y), cnt in zip(((1,0),(0,1),(-1,0),(0,-1)), [x2-x1, y2-y1]*2):
            for i in range(cnt):
                Array[Y][X] = hashmap[Array[Y][X]]
                Y, X = Y + y, X + x
    return result