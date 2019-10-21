					###Remove Duplicates from Sorted List II###

# Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
# For example,
# Given 1->2->3->3->4->4->5, return 1->2->5.
# Given 1->1->1->2->3, return 2->3.


class Solution(object):
    def deleteDuplicates(self, head):
        dummy = curr = ListNode(0)
        dummy.next = head
        
        while head and head.next:
            if head.val == head.next.val:
                while head and head.next and head.val == head.next.val:
                    head = head.next
                head = head.next
                curr.next = head
            else:
                curr.next = head
                curr = curr.next
                head = head.next
        return dummy.next        
