class Solution {

    // Input: arr of nums (sorted), target (int)
    // Output: Index of the number in the array or -1 if absent

    // Edge Case: Empty array -> -1

    // PLAN:
    // 1a. Create left and right indices
    // 1. Check the middle, compare it with the target ([while] looping with the index, number)
    // 2. If middle == target, return the index;
    //       middle > target, move right = middle - 1
    //       middle < target, move left = left + 1
    // 3. If left > right, return -1  

    // Time: O(log n). Space: O(1)
    fun search(nums: IntArray, target: Int): Int {
        var left = 0
        var right = nums.size - 1

        if (nums.size == 0) return -1

        while (left <= right) {
            val middleIndex = (left + right) / 2
            val middle = nums[middleIndex]
            
            if (middle == target)
                return middleIndex
            else if (middle > target) {
                right = middleIndex - 1
            }
            else {
                left = middleIndex + 1
            }
        }

        return -1
    }
}
