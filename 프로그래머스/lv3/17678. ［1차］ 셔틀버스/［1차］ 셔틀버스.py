def solution(n, t, m, timetable):
    timetable = [int(cr.split(':')[0])*60 + int(cr.split(':')[1]) for cr in timetable]
    timetable.sort()
    
    bus, i = dict(), 0
    for b in range(540, 540 + t*n, t):
        mem = []
        while len(mem) < m and i < len(timetable):
            if timetable[i] <= b:
                mem.append(timetable[i])
                i += 1
            else:
                break
        bus[b] = mem

    t = max(bus[b]) - 1 if len(bus[b]) == m else b
    return ':'.join(map(lambda s: f'{s:02}', divmod(t, 60)))