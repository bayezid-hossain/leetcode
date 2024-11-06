# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None or k==0:
            return head
        count=1
        last=head
        while last.next is not None:
            last=last.next
            count+=1
        k=k%count
        if k==0:
            return head
        newTail=head
        for _ in range(1,count-k):
            newTail=newTail.next
        newHead=newTail.next
        newTail.next=None
        last.next=head
        return newHead