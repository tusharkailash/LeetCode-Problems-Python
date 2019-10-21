										###Insertion Sort List:###



class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.next))
        else:
            return "Nil"

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = curr=  ListNode(0)
        dummy.next = head
        if not head:
            return None
        while head and head.next:
            if head.val <= head.next.val:
                head = head.next
            else:
                curr =dummy
                while curr.next.val < head.next.val:
                    curr = curr.next
                temp = head.next
                head.next = temp.next
                temp.next = curr.next
                curr.next = temp
        return dummy.next   


head = ListNode(7)
head.next = ListNode(1)
head.next.next = ListNode(4)
print Solution().insertionSortList(head)
