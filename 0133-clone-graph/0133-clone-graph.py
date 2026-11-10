"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        if node is None:
            return None

        visited = {}

        def dfs(node):
            # Return existing clone if already visited
            if node in visited:
                return visited[node]

            # Create a new node
            clone = Node(node.val)

            # Save it before exploring neighbors
            visited[node] = clone

            # Clone all neighbors
            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone

        return dfs(node)