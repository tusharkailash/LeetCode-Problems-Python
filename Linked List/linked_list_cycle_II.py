							### Linked List Cycle II ###

# Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
# Note: Do not modify the linked list.
# https://www.youtube.com/watch?v=Tf2M3pRaJSo


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                fast = head
                while slow != fast:
                    fast = fast.next
                    slow = slow.next
                return fast   #or return slow
        return None    
