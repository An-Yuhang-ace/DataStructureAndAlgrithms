# https://leetcode.cn/problems/linked-list-cycle-ii/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head):
        if head == None:
            return None
        slow, fast = head, head.next
        while slow != fast:
            if slow != None:
                slow = slow.next
            if fast != None:
                if fast.next != None:
                    fast = fast.next.next
                else:
                    fast = fast.next    
        if slow == None:
            return None
        else:
            slow = slow.next
            fast = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow