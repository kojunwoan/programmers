def solution(n, t, m, timetable):
    timetable = [int(cr[:2])*60 + int(cr[-2:]) for cr in timetable]
    timetable.sort()
    
    bus, i, l_t = dict(), 0, len(timetable)
    for b in range(540, 540 + t*n, t):
        mem = []
        while len(mem) < m and i < l_t:
            if timetable[i] <= b:
                mem.append(timetable[i])
                i += 1
            else:
                break
        bus[b] = mem

    t = bus[b][-1] - 1 if len(bus[b]) == m else b
    return f'{t//60:02}:{t%60:02}'