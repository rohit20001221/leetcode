from collections import deque as dque

class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

def BFSTree(root):
    ans = []

    if root is None:
        return ans
    
    queue = dque([root])

    while queue:
        n = len(queue)
        temp = []
        for i in range(n):
            el = queue.popleft()
            temp.append(el.value)

            if el.right:
                queue.append(el.right)
            
            if el.left:
                queue.append(el.left)
        
        ans.append(temp)
        temp = []
    
    return ans

root = Node(10)
root.right = Node(20)
root.left = Node(5)
root.left.left = Node(8)
root.right.left = Node(3)
root.right.right = Node(7)

print(BFSTree(root))