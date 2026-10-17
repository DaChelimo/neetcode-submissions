class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Return smaller, larger ... 1-indexed output ... do not reuse elements

        left, right = 0, len(numbers) - 1

        while left < right:
            total = numbers[left] + numbers[right]

            if total == target:
                return [left + 1, right + 1]
            elif total < target:
                left += 1
            elif total > target:
                right -= 1
        
        return []

        