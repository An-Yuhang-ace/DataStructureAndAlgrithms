# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head:[ListNode], n: int) -> [ListNode]:
        hair = ListNode(0, head)
        a = hair
        b = head
        for i in range(n):
            b = b.next

        while b != None:
            a = a.next
            b = b.next
        a.next = a.next.next

        return hair.next