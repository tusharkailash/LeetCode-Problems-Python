							###Intersection of Two Linked Lists###

							
# Write a program to find the node at which the intersection of two singly linked lists begins.
# For example, the following two linked lists:
# A:          a1 → a2
                   # ↘
                     # c1 → c2 → c3
                   # ↗            
# B:     b1 → b2 → b3
# begin to intersect at node c1.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None
        currA = headA  
        currB = headB
        while currA != currB:
            if currA:
                currA = currA.next
            else:
                currA = headB
            if currB:
                currB = currB.next
            else:
                currB=headA
        return currB        