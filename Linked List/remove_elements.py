
						###Remove Linked List Elements###

# Example
# Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
# Return: 1 --> 2 --> 3 --> 4 --> 5


class Solution(object):
    def removeElements(self, head, val):
        dummy = curr = ListNode(-1)
        dummy.next = head
        
        while curr and curr.next:
            if curr.next.val == val :
                curr.next = curr.next.next
            else:
                curr = curr.next
                
        return dummy.next      
