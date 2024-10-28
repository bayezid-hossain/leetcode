# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def max_depth(root,res):
            if not root:
                return 0
            
            left=max_depth(root.left,res)
            right=max_depth(root.right,res)

            res[0]=max(res[0],left+right)
            return max(left,right)+1
        res=[0]
        max_depth(root,res)
        return res[0]
        