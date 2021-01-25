# RIGHT ROOT LEFT

class Node:
    def __init__(self, val, right=None, left=None):
        self.val = val
        self.right = right
        self.left = left

def preOrder(root):

    if root:
        preOrder(root.right)
        print(root.val)
        preOrder(root.left)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

preOrder(root)