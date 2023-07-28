def solution(n, results):
    res_d = {i: {j: None for j in range(1, n + 1) if i != j} for i in range(1, n + 1)}

    def win_lose(win, lose):
        if res_d[win][lose] is None:
            res_d[win][lose] = True
            res_d[lose][win] = False
            for l_lose, l_res in res_d[lose].items():
                if l_res == True:
                    win_lose(win, l_lose)
            for w_win, w_res in res_d[win].items():
                if w_res == False:
                    win_lose(w_win, lose)
    
    for win, lose in results:
        win_lose(win, lose)
        
    return sum(None not in d.values() for d in res_d.values())