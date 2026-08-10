from collections import defaultdict
import heapq

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

    
    # 2. WITH MIN-HEAP
    # Create a dict (key -> num, value -> occ)
    # Create a heap
    # Enumerate through dict (num, occ). 
    # Check heap size; if size > k, heap.pop
    # Otherwise, push (occ, num) 
    # convert heap to list, by selecting the item[1]
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = defaultdict(int)

        for num in nums:
            freq_map[num] += 1
        
        freq_min_heap = []
        
        for num, freq in freq_map.items():
            heapq.heappush(freq_min_heap, (freq, num))

            if len(freq_min_heap) > k:
                heapq.heappop(freq_min_heap)
        
        result = []

        for pair in freq_min_heap:
            result.append(pair[1])

        return result




    # Given an arr with fully unique nums, our list can be of max size len(arr)
    # Create an arr of arrs called tracker

    # 1. Create a dict of key (number) and value (occurrence)
    # 1b. Tie every index in the arr ----- number of occurrences of that element
    # 2. Enumerate (num, occ) through that dict, and then get the list at the index (occ),
    # 3. Append that num to the list you get
    # 4. tracker -> [[], [2,3], [4]] -> [2, 3, 4, 4]
    # 5a. Create a result list
    # 5b. Loop IN REVERSE through tracker, get list, and append the items in the list, until we get
    #     to len k, and then return result

    # Time: O(n). Space: O(n)

    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     occurence_map = defaultdict(int)

    #     for num in nums:
    #         occurence_map[num] += 1
        
    #     tracker = [[] for i in range(len(nums) + 1)]

    #     for num, occ in occurence_map.items():
    #         tracker[occ].append(num)


    #     result = []

    #     for i in range(len(tracker) - 1, 0, -1):
    #         curr_list = tracker[i]

    #         for elem in curr_list:
    #             result.append(elem)

    #             if len(result) == k:
    #                 return result
        
    #     return []







