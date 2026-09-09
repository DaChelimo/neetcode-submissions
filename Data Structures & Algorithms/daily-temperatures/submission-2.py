class Solution:
    # Input: arr temperatures 
    # Output: arr result[i] -> number of days after which the temp rises

    # Remember: if temp does not get higher in the future, 
    # put 0 in that position
    # Cases: Decreasing list -> [0, 0, 0]. 
    # Increasing -> [1, 1, 1]. Similar numbers: [20, 20, 21] -> [2, 1, 0]

    # # PLAN:
    # # 1. Loop through the list with a pointer i
    # # 2. Create j += 1. Loops until it finds a greater one.
    # # 3. Diff = j - i. Set result[i] = diff

    # # Time: O(n ^2). Space: O(n) 
    # def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    #     length = len(temperatures)
    #     res = [0] * length

    #     for i in range(length):
    #         j = i + 1

    #         while j < length and temperatures[j] <= temperatures[i]:
    #             j += 1
            
    #         if j != length: 
    #             # While loop terminated because the array was exhausted
    #             res[i] = j - i
            
    #     return res
    
    # Create an array inited to 0s
    # Create a stack containing (elem, index)
    # Loop through the temp array
    # Check the top stack value (should be the lowest of them all)
    # while top stack value < current, pop stack, and update the elem
    # position in the result array
    
    # Time: O(n). Space: O(n)
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [] # (elem, index)

        for index, elem in enumerate(temperatures):
            while stack and stack[-1][0] < elem:
                popped = stack.pop()
                popped_index = popped[1]
                result[popped_index] = index - popped_index
            
            stack.append([elem, index])

        return result
