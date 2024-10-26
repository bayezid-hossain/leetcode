# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        max_d=0
        queue=deque([(root,1)])

        while queue:
            length=len(queue)
            for _ in range(length):
                curr,distance=queue.popleft()

                if curr.left:
                    queue.append([curr.left,distance+1])
                    
                if curr.right:
                    queue.append([curr.right,distance+1])
                max_d=max(max_d,distance)

        return max_d          