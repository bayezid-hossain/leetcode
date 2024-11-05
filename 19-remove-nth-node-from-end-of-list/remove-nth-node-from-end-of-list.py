# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp=head
        count=0
        while temp!=None:
            count+=1
            temp=temp.next
        havetogo=count-n
        if havetogo==0:
            if count==1:
                return None
            else:
                return head.next
        temp=head
        for i in range(havetogo-1):
            temp=temp.next
        temp.next=temp.next.next
        return head