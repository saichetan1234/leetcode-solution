# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def check(root):
            if not root:
                return None
            if root.left or root.right:
                temp=root.left
                root.left=root.right
                root.right=temp
            check(root.left)
            check(root.right)
        check(root)
        return root