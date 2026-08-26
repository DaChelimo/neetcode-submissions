/**
 * Definition for a binary tree node.
 * class TreeNode(var `val`: Int) {
 *     var left: TreeNode? = null
 *     var right: TreeNode? = null
 * }
 */

class Solution {
    // Recursion
    // BC: root is None, return None
    // RC: swap left and right: temp = root.right ; 
    //     root.right = root.left ; root.left = temp
    //      recurse on root.left and root.right
    
    // Time: O(log n). Space: O(log n)
    fun invertTree(root: TreeNode?): TreeNode? {
        if (root == null)
            return null
        
        var rightTemp = root.right
        root.right = invertTree(root.left)
        root.left = invertTree(rightTemp)

        return root
    }
}
