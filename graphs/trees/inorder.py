# LEFT ROOT RIGHT

class Node:
    def __init__(self, val, right=None, left=None):
        self.val = val
        self.right = right
        self.left = left

def inOrder(root):

    if root:
        inOrder(root.left)
        print(root.val)
        inOrder(root.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

inOrder(root)