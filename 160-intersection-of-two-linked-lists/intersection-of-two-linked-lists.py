# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        map={}
        while headA is not None:
            map[headA]=headA.val
            headA=headA.next
        while headB is not None:
            if headB in map:
                return headB
            map[headB]=headB.val
            headB=headB.next
        return None