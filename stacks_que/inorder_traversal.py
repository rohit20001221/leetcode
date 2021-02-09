# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        self.inOrderHelper(root, ans)
        return ans
    
        
    def inOrderHelper(self, root, ans):
        if root:
            self.inOrderHelper(root.left, ans)
            ans.append(root.val)
            self.inOrderHelper(root.right, ans)