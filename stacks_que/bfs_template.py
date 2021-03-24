from collections import deque

def BFS(root, goal):
    Q = deque([root])
    visited = [root]

    while !(Q.empty()):
        v = Q.popleft()
        if v is goal:
            return v
        
        for v_ in v.neighbours():
            if v_ not in visited:
                visited.append(v_)
                q.append(v_)


