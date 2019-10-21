                              			###Remove Nth Node From End of List###       

#Given a linked list, remove the nth node from the end of list and return its head.
#For example,
#   Given linked list: 1->2->3->4->5, and n = 2.
#
#   After removing the second node from the end, the linked list becomes 1->2->3->5.
#Note:
#Given n will always be valid.
#Try to do this in one pass.
 

# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = temp = ListNode(0)
        dummy.next = head
        
        for i in range(n):
            head = head.next
        
        while head:
            head = head.next
            temp = temp.next
        
        temp.next = temp.next.next
        return dummy.next
