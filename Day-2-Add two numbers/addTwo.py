# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: Optional[ListNode]) ->    Optional[ListNode]:
        current = headposition = ListNode(0)
        carryBit = 0
        while l1 or l2 is not None or carryBit is not 0:
            firstVal = l1.val if l1 != None else 0
            secondVal = l2.val if l2 != None else 0
            current.next = ListNode((firstVal + secondVal + carryBit)%10)
            current = current.next
            carryBit = (firstVal + secondVal + carryBit)//10
            l1=l1.next if l1 != None else None
            l2=l2.next if l2 != None else None
        return headposition.next