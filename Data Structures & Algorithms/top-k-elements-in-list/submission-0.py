from collections import defaultdict

class Solution:

    # INPUT: int arr (nums), int k
    # OUTPUT: k most frequent elements in arr (in any order -> one solution)

    # Edge Cases:
    # 1. arr is empty, one element -> return the element
    # 2. k is 0, return []

    # Plan
    #  (loop through every elem at least once)
    # 1. Create a default dict (key -> number, value -> num of occurrences)
    # 2. Loop through the list, and update the dict accordingly
    # 3. Sort the dict (based on the values)
    # 3b. Returning the top k elements

    # ISSUE: {a -> 3, b -> 4, c -> 3 ...}

    # 1. Do an initial pass and get num of unique elements (using a hashset)
    # 2. Create an arr of len Unique, 

    # 1. Create Counter dict
    # 2. Sort by value, and get the key as an array
    # 3. Return the first k elements

    # Time: O(n log n). Space: O(n)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for elem in nums:
            count[elem] += 1
        
        count = [number for number, occurrence in sorted(count.items(), key = lambda item: item[1], reverse = True)]

        return count[:k]
