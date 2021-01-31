def DFS(cur, target, visited):
    if cur == target:
        return True
    
    for next_ in cur.neighbors():
        if next_ not in visited:
            visited.append(next_)
            return DFS(next_, target, visited)
    
    return False
    