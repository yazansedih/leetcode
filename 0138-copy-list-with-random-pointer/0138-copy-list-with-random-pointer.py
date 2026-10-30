class Solution(object):
    def copyRandomList(self, head):
        if not head:
            return None

        copies = {}

        # Step 1: Create a copy of every node
        current = head

        while current:
            copies[current] = Node(current.val)
            current = current.next

        # Step 2: Connect next and random pointers
        current = head

        while current:
            copies[current].next = copies.get(current.next)
            copies[current].random = copies.get(current.random)

            current = current.next

        # Step 3: Return the copied list
        return copies[head]