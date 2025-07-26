# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        ans=[0]
        def check(root,curr,inc):
            if not root:
                return 0
            if root.val+curr==targetSum:
                ans[0]+=1
            if inc==1:
                check(root.left,curr+root.val,1)
                check(root.right,curr+root.val,1)
            else:
                check(root.left,curr,0)
                check(root.right,curr,0)
                check(root.left,curr+root.val,1)
                check(root.right,curr+root.val,1)
        check(root,0,0)
        return ans[0]
        