def DFS_Recursive(v,visited):
    visited[v] = True

    for neighbour in v.neighbours():
        if not visited[neighbour]:
            DFS_Recursive(v, visited)

def DSF(v, visited):
    stack = []
    stach.append(v)

    while len(stack) > 0:
        v_ = stack.pop()
        if not visited[v_]:
            visited[v_] = True
            for neighbour in v_.neighbours():
                stack.push(neighbour)