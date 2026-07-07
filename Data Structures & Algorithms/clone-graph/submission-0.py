"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old_to_new = {}

        def dfs(node):
            if node is None: return None
            if node in old_to_new: return old_to_new[node]

            clone = Node(node.val) 

            old_to_new[node] = clone
            for neigh in node.neighbors:
                cloned_neighbor = dfs(neigh)
                clone.neighbors.append(cloned_neighbor)
            return clone

        return dfs(node) 
            
