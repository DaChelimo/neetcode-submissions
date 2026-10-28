"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    # 1. Create a map of node to duplicateNode
    # 2. Recurse on duplicate
    # 2b. Create a new Node, as well as list of Nodes (neighbors)
    # 3. If duplicate is in tracker, return tracker[duplicate]
    # 3b. Create node, and duplicate neighbors

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        tracker = {}

        def duplicate(node: Optional['Node']) -> Optional['Node']:
            if not node:
                return None
            if node in tracker:
                return tracker[node]
            
            tracker[node] = Node(node.val)
            
            for nei in node.neighbors:
                newNei = duplicate(nei)
                tracker[node].neighbors.append(newNei)
            
            return tracker[node]

        return duplicate(node)