# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    inorder_map=[]
    index=-1
    def __init__(self, root: Optional[TreeNode]):
        self.inorder_map=[]
        def inorder(start):
            if start is None:
                return
            
            inorder(start.left)
            self.inorder_map.append(start)
            inorder(start.right)
        inorder(root)

    def next(self) -> int:
        self.index+=1
        # print(len(self.inorder_map))
        return self.inorder_map[self.index].val
        

    def hasNext(self) -> bool:
        
        return True if self.index+1<len(self.inorder_map) else False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()