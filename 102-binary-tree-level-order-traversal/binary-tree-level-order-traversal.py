# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        result=[]
        
        def bfs(root):
            nonlocal result
            if not root:
                
                return []

            queue=deque([root])
            while queue:
                
                temp = []
                length=len(queue)
                for _ in range(length):
                    
                    current = queue.popleft()
                    temp.append(current.val)
                    if current.left:
                        queue.append(current.left)

                    if current.right:
                        queue.append(current.right)
                result.append(temp)
        bfs(root)
        return result