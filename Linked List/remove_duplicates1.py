									### Remove Duplicates from Sorted List I ###
									
# Given a sorted linked list, delete all duplicates such that each element appear only once.
# For example,
# Given 1->1->2, return 1->2.
# Given 1->1->2->3->3, return 1->2->3.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# return back the head of the linked list in the below method.


def RemoveDuplicates(head):
    if head is None:
        return head
    Node=head
    while Node.next:
        if Node.data==Node.next.data:
             Node.next = Node.next.next
        else:    
             Node= Node.next
    return head        

#Second Solution:

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        curr = head
        headB = curr.next
        while curr and headB:
            if curr.val == headB.val:
                curr.next = headB.next
                headB = headB.next
            else:
                curr  = headB 
                headB=headB.next

        return head
