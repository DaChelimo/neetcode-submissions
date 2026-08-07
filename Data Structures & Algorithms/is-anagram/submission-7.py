from collections import defaultdict

class Solution:
    
    # Create a dict of key (alpha): value (num of occurrences)
    # Compare both dict; return True if similar
    # Edge Case: Both Empty; Length differs, short circuit

    # Time: O(n + m). Space: O(1)
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_dict = defaultdict(int)
        t_dict = defaultdict(int)

        for i in range(len(s)):
            s_dict[s[i]] += 1
            t_dict[t[i]] += 1

        return s_dict == t_dict

    # Check len(S) == len(T)
    # Create a count array [len 26]
    # Loop through 0..len(s), s[i] -> increase it in its index in our arr count
    #                         t[i] -> decrease """"
    # Check if every char 
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26
        
        for i in range(len(s)):
            s_index = ord(s[i]) - ord('a')
            t_index = ord(t[i]) - ord('a')

            count[s_index] += 1 
            count[t_index] -= 1 
        
        for char in count:
            if char != 0:
                return False
        
        return True




        