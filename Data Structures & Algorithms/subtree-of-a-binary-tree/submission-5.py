# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    # Recursion:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        
        if self.isSameTree(root, subRoot):
            return True
        else:
            return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))
    

    def isSameTree(self, node: Optional[TreeNode], clone: Optional[TreeNode]) -> bool:
        if not node and not clone:
            return True
        
        if not node or not clone:
            return False

        if node.val == clone.val:
            left = self.isSameTree(node.left, clone.left)
            right = self.isSameTree(node.right, clone.right)
            return left and right
        else:
            return False

            