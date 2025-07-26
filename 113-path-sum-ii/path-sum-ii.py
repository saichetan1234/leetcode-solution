# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans=[]
        def check(root,curr,path):
            if not root:
                return None
            path.append(root.val)
            if not root.left and not root.right and curr==root.val:
                ans.append(path[:])
            check(root.left,curr-root.val,path)
            check(root.right,curr-root.val,path)
            path.pop()
            
        check(root,targetSum,[])
        return ans
        