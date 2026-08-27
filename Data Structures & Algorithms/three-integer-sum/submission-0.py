class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        result = []

        for i, num in enumerate(nums):
            if num > 0: # All nums positive hence can not be 0
                continue
            
            if i > 0 and nums[i - 1] == num: # Skip duplicate
                continue
            

            j = i + 1
            k = len(nums) - 1

            while (j < k):
                total = nums[j] + nums[k] + num
                
                if (total < 0):
                    j += 1
                elif (total > 0):
                    k -= 1
                else:
                    result.append([num, nums[j], nums[k]])

                    k -= 1
                    j += 1

                    while (j - 1 > i and j < k and nums[j] == nums[j - 1]):
                        j += 1
    
        return result

            

