def solution(fees, records):
    board = {}
    park = {}
    
    for re in records:
        t, n, s = re.split()
        t = int(t[:2])*60 + int(t[-2:])
        if s == 'IN':
            park[n] = t
        else:
            board.setdefault(n, 0)
            board[n] += t - park.pop(n)
    else:
        t = 23*60 + 59
        for n, p in park.items():
            board.setdefault(n, 0)
            board[n] += t - p
        
    return [fees[1] + max(-(-(v-fees[0])//fees[2]), 0) * fees[3] for k, v in sorted(board.items(), key=lambda x: x[0])]