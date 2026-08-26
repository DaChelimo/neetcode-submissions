# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Recursion
    # BC: root = None, return 0
    # Get the height of left and right tree
    # Return 1 + max(left, right)
    # Time: O(n) where n is height of tree. Space: O(n)
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return 1 + max(left, right)

        