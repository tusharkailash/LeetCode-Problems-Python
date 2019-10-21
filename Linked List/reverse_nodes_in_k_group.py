                                        ###Reverse Nodes in k-Group###

# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
# You may not alter the values in the nodes, only nodes itself may be changed.
# Only constant memory is allowed.
# For example,
# Given this linked list: 1->2->3->4->5
# For k = 2, you should return: 2->1->4->3->5
# For k = 3, you should return: 3->2->1->4->5


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.next))
        else:
            return "Nil"
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # 1 -> 2 -> 3 -> 4 -> 5

        len = self.find_length(head)
        n = len/k

        dummy = curr = ListNode(0)
        dummy.next = head

        if not head:
            return None

        for i in range(n):
            prev = None
            start = head
            for i in range(k):
                temp = head.next
                head.next = prev
                prev = head
                head = temp
            curr.next = prev
            curr = start
            curr.next = head
        return dummy.next

    def find_length(self,head):
        count = 0
        while head:
            head = head.next
            count += 1
        return count


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
print Solution().reverseKGroup(head,2)
