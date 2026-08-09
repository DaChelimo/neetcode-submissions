from collections import Counter

class Solution:

    # Input: List of str (strs)
    # Output: List of sublists (each is a bunch of anagrams)

    # APPROACH 1:
    # 1. Sort every word
    # 2. Build a dict
    # 3. If sorted word in dict, add word to the list (value) of that dict
    # 4. Return a list containing all the lists in the dict (values)
    # Time: O(n * m log m). Space: O(n * m)


    # APPROACH 2:
    # 1. Create counters for each word, append to list
    # 2. Loop through list, and create dict [key -> counter, value -> word]
    # 3. Return list of all the lists
    # Time: O(n * m). Space: O(n)

    # APPROACH 3: Uses arrays ([0] * 26)
    # 1. Create array of size 26 for each word
    # 2. Loop through the word, and increase the count for the position of each char
    #    (aabc -> [211....000])
    # 3. Convert the arr to tuple, use it as key to dict
    # 4. Group words in the dict based on that tuple
    # 5. Return dict.values() [List[List[str]]]
    
    # Time: O(n * m). Space: O(n)

    # Constraints: 1 element / empty string -> sublist in a list
    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #     word_map = dict()

    #     for word in strs:
    #         word_counter = frozenset(Counter(word).items())
    #         word_map[word_counter] = word_map.get(word_counter, []) + [word]
        
    #     return list(word_map.values())

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_map = dict()

        for word in strs:
            alpha = [0] * 26
            
            for char in word:
                index = ord(char) - ord('a')
                alpha[index] += 1
            
            alpha = tuple(alpha)
            word_map[alpha] = word_map.get(alpha, []) + [word]
        
        return list(word_map.values())

