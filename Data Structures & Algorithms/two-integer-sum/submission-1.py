class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Hashmap -> Key: 3, value: index (0)

        # loop through nums
        # subtracting target - currentNumber  3
        # check whether in the map true
        # 0, 1

        numbersMap = {}

        for index, num in enumerate(nums):
            complement = target - num

            if (complement in numbersMap):
                smallerIndex = numbersMap[complement]
                return [smallerIndex, index]
            
            numbersMap[num] = index


