# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        
        small_dummy = ListNode(0)
        tail_dummy = ListNode(0)

        small = small_dummy
        large = tail_dummy
        
        current = head

        while current:
            next_node = current.next

            if current.val < x:
                small.next = current
                small = small.next
            else:
                large.next = current
                large = large.next

            current = next_node

        large.next = None
        small.next = tail_dummy.next
        
        return small_dummy.next


