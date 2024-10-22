# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result=[]

        def pre(root):
            nonlocal result
            if root is None:
                return
            
            result.append(root.val)
            pre(root.left)
            pre(root.right)
        pre(root)
        return result
        