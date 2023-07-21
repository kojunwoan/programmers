def solution(n, computers):
    group = 0
    queue = []
    visited = set()
    
    for i, node in enumerate(computers):
        if i not in visited:
            queue.append(node)
            visited.add(i)
            group += 1
            
        while queue:
            for i, node in enumerate(queue.pop(0)):
                if node and i not in visited:
                    queue.append(computers[i])
                    visited.add(i)
    
    return group