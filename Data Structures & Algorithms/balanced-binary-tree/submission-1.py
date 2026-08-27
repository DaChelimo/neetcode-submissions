# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Recursion
    # BC: root is None -> return 0
    # RC: At node x, compare left and right, 
    #     If the diff > 1, return -1
    #     Otherwise, return the height -> longest + 1
    # in every iteration, check if result == -1, return -1
    # If -1, return False. Else, return True

    #: Time: O(n). Space: O(h)
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node: Optional[TreeNode]):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            if left == -1 or right == -1:
                return -1

            if abs(right - left) > 1:
                return -1
            
            return 1 + max(left, right)
        
        height = dfs(root)

    
        return height != -1
        
