# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Recursion
    # BC: p = q = None -> return True
    #       p = None and q != None -> False (vice - versa)
    # RC: p = q =!= None
    #     p.val == q.val and recurse on p.left and q.left, same for right

    # Time: O(n). Space: O(h)
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False
        
        if p.val != q.val:
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        