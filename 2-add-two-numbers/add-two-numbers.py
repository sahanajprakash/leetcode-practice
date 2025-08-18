# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        ret = res
        c = 0
        while l1 is not None and l2 is not None:
            curSum = l1.val + l2.val + c
            res.next = ListNode(curSum % 10)
            c = curSum // 10
            res = res.next
            l1 = l1.next
            l2 = l2.next
        
        if l1 is not None:
            while l1:
                curSum = c + l1.val
                c = curSum // 10
                res.next = ListNode(curSum % 10)
                res = res.next
                l1 = l1.next
        
        if l2 is not None:
            while l2:
                curSum = c + l2.val
                c = curSum // 10
                res.next = ListNode(curSum % 10)
                res = res.next
                l2 = l2.next
        
        if c:
            res.next = ListNode(c)
        
        return ret.next
