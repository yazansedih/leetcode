# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):

        dummy = ListNode(0)
        dummy.next = head

        prev = dummy

        # Move prev to the node before left
        for _ in range(left - 1):
            prev = prev.next

        current = prev.next

        # Reverse the sublist
        for _ in range(right - left):

            next_node = current.next

            temp = prev.next
            
            current.next = next_node.next

            next_node.next = temp

            prev.next = next_node


        return dummy.next