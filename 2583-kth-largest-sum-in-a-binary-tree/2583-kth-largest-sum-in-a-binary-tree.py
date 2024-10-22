# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        levels_sum =[]
        def BFS(root):
            nonlocal levels_sum
            queue = deque([root])
            while queue:
                level_sum = 0
                queue_size = len(queue)
                for _ in range(queue_size):
                    node = queue.popleft()
                    level_sum += node.val
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                levels_sum.append(level_sum)
        BFS(root)
        if len(levels_sum)<k:
            return -1
        levels_sum.sort(reverse=True)
        return levels_sum[k-1]


