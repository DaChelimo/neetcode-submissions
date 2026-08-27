class Solution:
    # Create two pointers (left, right)
    # Calculate the area [(dist * min(left, right))] using left and right, and compare with the max
    #  Update the max accordingly
    # Move the smaller one
    # Stop when they overlap

    # Time: O(n). Space: O(1)
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1

        result = 0

        while left < right:
            dist = right - left
            area = dist * min(heights[left], heights[right])

            result = max(area, result)

            if (heights[left] < heights[right]):
                left += 1
            else:
                right -= 1
            
        return result

        