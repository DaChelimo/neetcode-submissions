class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # Key number, Value index

        for i, num in enumerate(nums):
            partner = target - num
            
            if partner in seen:
                j = seen[partner]
                return [j, i]
            
            seen[num] = i
        
        return []