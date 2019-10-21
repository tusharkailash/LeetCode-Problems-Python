						###Palindrome Linked List###
						
#Given a singly linked list, determine if it is a palindrome.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next       # mid point found here
        
        Node = None
        while slow:
            next = slow.next
            slow.next = Node
            Node = slow
            slow = next            # reversed the second half of linked list 
        
        #check the first half of linked list with second half
        
        while Node:
            if head.val != Node.val:
                return False
            Node = Node.next
            head = head.next
        return True    
