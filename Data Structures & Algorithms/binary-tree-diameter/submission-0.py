# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Recursion
    # BC: Root == None, return 0
    # RC: getHeight of left and right tree, store them
    #     calculate the dist of that path, compare with the max, update max accordingly
    #     return the longer tree + 1
    
    # Time: O(n). Space: O(h)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiameter = 0

        def dfs(node: Optional[TreeNode]):
            nonlocal maxDiameter

            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            diameter = left + right
            maxDiameter = max(maxDiameter, diameter)

            return 1 + max(left, right)
        
        dfs(root)

        return maxDiameter

        