from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

def ZigZagTree(root):
    result = []

    if root is None:
        return result
    
    q = deque([root])
    zigzag = False

    while q:
        level = []
        n = len(q)

        for _ in range(n):
            if zigzag:
                node = q.pop()
                level.append(node.value)

                if node.right:
                    q.appendleft(node.right)
                
                if node.left:
                    q.appendleft(node.left)
            else:
                node = q.popleft()
                level.append(node.value)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)
                
        result.append(level)
        level = []
        zigzag = not zigzag

    return result            



root = Node(10)
root.right = Node(20)
root.left = Node(5)
root.left.left = Node(8)
root.right.left = Node(3)
root.right.right = Node(7)

print(ZigZagTree(root))