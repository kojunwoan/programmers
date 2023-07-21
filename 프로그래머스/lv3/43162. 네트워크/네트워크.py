def solution1(n, computers): #BFS
    group = 0
    queue = []
    visited = set()
    
    for i, computer in enumerate(computers):
        if i not in visited:
            queue.append(computer)
            visited.add(i)
            group += 1
            
        while queue:
            for i, v in enumerate(queue.pop(0)):
                if v and i not in visited:
                    queue.append(computers[i])
                    visited.add(i)
    
    return group

def solution(n, computers): #DFS
    group = 0
    visited = set()
    
    def dfs(computer):
        for j, v in enumerate(computer):
            if v and j not in visited:
                visited.add(j)
                dfs(computers[j])
    
    for i, computer in enumerate(computers):
        if i not in visited:
            visited.add(i)
            group += 1
            dfs(computer)
    
    return group