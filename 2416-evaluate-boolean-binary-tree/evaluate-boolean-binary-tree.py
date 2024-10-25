# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        
        def eval(root):
            
            if root.val==0:
                return False
            elif root.val==1:
                return True
            elif root.val==2:
                return eval(root.left) or eval(root.right)
            elif root.val==3:
                return eval(root.left) and eval(root.right)
            
        return eval(root)