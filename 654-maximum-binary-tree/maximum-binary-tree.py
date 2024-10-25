# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        
        root=TreeNode()
        
        def buildTree(node,array):
            if not node:
                return None
            node.val=max(array)
            index=0
            for i in range(len(array)):
                if array[i]==node.val:
                    index=i
                    break
            leftprefix=array[0:index]
            rightsuffix=array[index+1:]
            leftnode=None
            rightnode=None
            if len(leftprefix)>0:
                leftnode=TreeNode(0)
            if len(rightsuffix)>0:
                rightnode=TreeNode(0)
            node.left=(buildTree(leftnode,leftprefix))
            node.right=buildTree(rightnode,rightsuffix)
            
            
            return node
        return buildTree(root,nums)
            