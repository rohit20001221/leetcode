from collections import deque

def BFS(root, target):
    queue = deque([root])
    step = 0

    while(queue):
        step += 1
        size = len(queue)

        for i in range(size):
            cur = queue.popleft()

            if cur == target:
                return step
            
            for next_ in cur.neighbours():
                queue.append(next_)
            
    return -1
