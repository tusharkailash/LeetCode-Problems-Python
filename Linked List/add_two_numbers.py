									###Add Two Numbers###

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = curr = ListNode(0)
        carry = 0
        
        while l1 or l2:
              a= l1.val if l1 else 0
              b = l2.val if l2 else 0
              sum = a + b + carry
              
              curr.next = ListNode(sum%10)
              curr = curr.next
              carry = sum/10
              
              if l1:
                  l1 = l1.next
              if l2:
                  l2 = l2.next
        if carry > 0:
            curr.next = ListNode(1)
        return dummy.next          
