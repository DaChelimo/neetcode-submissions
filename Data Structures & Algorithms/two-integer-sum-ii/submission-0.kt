class Solution {
    // INPUT: numbers array, target int
    // OUTPUT: Indices of two nums that add up to target 
    
    // IMPORTANT: (index1 < index). Array is sorted ascending.index1 != index2
    // Therefore, if we get to left == right, we should stop since that would give
    // us the same value for the indicies

    // PLAN
    // 1. Create two pointers (left, right)
    // 2. Add up the ends, and if the sum > target, move end -= 1
    // 3. If sum < target, move left += 1
    // 4. If sum = target, return [left, right]
    
    // Time: O(n). Space: O(1)
    fun twoSum(numbers: IntArray, target: Int): IntArray {
        var left = 0
        var right = numbers.size - 1

        while (left < right) {
            val sum = numbers[left] + numbers[right]

            if (sum == target) {
                return intArrayOf(left + 1, right + 1)
            }
            else if (sum > target) {
                right--
            }
            else {
                left++
            }
        }

        return intArrayOf()
    }
}
