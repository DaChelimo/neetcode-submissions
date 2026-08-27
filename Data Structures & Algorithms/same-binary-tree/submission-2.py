# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # # Recursion
    # # BC: p = q = None -> return True
    # #       p = None and q != None -> False (vice - versa)
    # # RC: p = q =!= None
    # #     p.val == q.val and recurse on p.left and q.left, same for right

    # # Time: O(n). Space: O(h)
    # def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    #     if not p and not q:
    #         return True
    #     elif not p or not q:
    #         return False
        
    #     if p.val != q.val:
    #         return False
    #     else:
    #         return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    # Iteratively
    # Create a stack [(left, right)]
    # Loop through using while on the stack
    # If the popped nodes are different, break out and return False
    # Else, continue while adding (node.left, node.right) to the stack

    # Time: O(n). Space: O(n)
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p, q)]

        while stack:
            node1, node2 = stack.pop()

            if not node1 and not node2:
                continue
            if not node1 or not node2:
                return False

            if node1.val == node2.val:
                stack.append((node1.left, node2.left))
                stack.append((node1.right, node2.right))
            else:
                return False
        
        return True

        