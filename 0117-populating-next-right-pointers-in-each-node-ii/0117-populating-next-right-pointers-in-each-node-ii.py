"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution(object):
    def connect(self, root):

        if not root:
            return None

        queue = [root]

        while queue:

            level_size = len(queue)

            for i in range(level_size):

                node = queue.pop(0)

                # Connect to the next node in the same level
                if i < level_size - 1:
                    node.next = queue[0] if queue else None

                # Add children to queue
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return root 