# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if head is None or k == 0:
            return head

        dummy = ListNode(0)
        dummy.next = head

        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next

        k %= length
        if k == 0:
            return head

        slow = dummy
        fast = dummy
        for _ in range(k):
            fast = fast.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        # Finaly
        new_head = slow.next
        slow.next = None

        fast.next = head

        return new_head
        