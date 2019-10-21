							###Rotate list###

# For example:
# Given 1->2->3->4->5->NULL and k = 2,
# return 4->5->1->2->3->NULL.

class Solution:  
    # @param head, a ListNode  
    # @param k, an integer  
    # @return a ListNode  
    def rotateRight(self, head, k):  
        if head == None or k == 0:  
            return head  
          
        length = 1  
        node = head  
        while node.next != None:  
            length += 1  
            node = node.next  
              
        m = k % length  
          
        node.next = head  
          
        for i in range(length - m):  
            node = node.next  
          
        head = node.next  
          
        node.next = None  
          
        return head  
