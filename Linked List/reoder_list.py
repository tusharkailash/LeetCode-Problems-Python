							###REORDER LIST###

# Given a singly linked list L: L0→L1→…→Ln-1→Ln,
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
# For example,
# Given {1,2,3,4}, reorder it to {1,4,2,3}.



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        if not head or not head.next:
            return 
        mid = self.getMid(head)
        rev.self=get.reverse(mid.next)
        mid.next = None
        self.merge(head,rev)
        
    def getMid(self,head):
        slow = head
        fast = fast.next
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next
        return slow
        
    def reverse(self,head):
        prev = None
        while head:
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp
        return prev    
        
    def merge(self,l,r):
        dummy = curr = ListNode(l,r)
        while l and r:
            curr.next = l
            curr  =l 
            l = l.next
            
            curr.next = r
            curr = r
            r = r.next
            
        if l:
            curr.next = l
        if r: 
            curr.next = r
