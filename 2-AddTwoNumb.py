# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s = l1.val + l2.val
        d = s // 10
        o = s % 10
        root = ListNode(o, None)
        nextLN = root
        finish = ListNode()
        while l1.next != None or l2.next != None or (l1.val + l2.val + d) // 10 != 0:
            if l1.next != None:
                l1 = l1.next
            else:
                l1 = ListNode()
            if l2.next != None:
                l2 = l2.next
            else:
                l2 = ListNode()
            if l1.next == None and l2.next == None and ((l1.val + l2.val + d) // 10 == 0):
                s = l1.val + l2.val + d
                finish = ListNode(s, None)
                nextLN.next = finish
                nextLN = finish
                break
            s = l1.val + l2.val + d
            d = s // 10
            o = s % 10
            tempLN = ListNode(o, None)
            nextLN.next = tempLN
            nextLN = tempLN
        return root
        