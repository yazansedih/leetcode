# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """

        length = 0 # length = 5
        temp = head
        while temp:
            length += 1
            temp = temp.next


        dummy = ListNode(0)
        prev = dummy

        prev.next = head

        for _ in range(length // k):
            
            current = prev.next
            for _ in range(k - 1):

                next_node = current.next

                current.next = next_node.next
                next_node.next = prev.next
                prev.next = next_node

            prev = current
                
        return dummy.next
        