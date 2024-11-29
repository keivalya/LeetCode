# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)  # Placeholder for the result
        current = dummy
        carry = 0
        while l1 or l2:
            carry += (l1.val if l1 else 0) + (l2.val if l2 else 0)
            current.next = ListNode(carry % 10)
            carry //= 10  # Update carry
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            current = current.next
        if carry:
            current.next = ListNode(carry)
        return dummy.next