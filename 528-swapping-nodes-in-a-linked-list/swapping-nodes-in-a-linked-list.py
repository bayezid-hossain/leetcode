# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        count=0
        cur=head
        front=None
        end=None
        while cur is not None:
            count+=1

            if count==k:
                front=cur
                end=head
            if count>k:
                end=end.next
            cur=cur.next
        
        front.val,end.val=end.val,front.val
        return head