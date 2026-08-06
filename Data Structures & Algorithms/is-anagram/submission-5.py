from collections import defaultdict

class Solution:
    
    # Create a dict of key (alpha): value (num of occurrences)
    # Compare both dict; return True if similar
    # Edge Case: Both Empty; Length differs, short circuit

    # Time: O(n). Space: O(n)
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_dict = defaultdict(int)
        t_dict = defaultdict(int)

        # You can do len(s) or len(t)
        for i in range(len(s)):
            s_dict[s[i]] += 1
            t_dict[t[i]] += 1


        # for char in s:
        #     s_dict[char] += 1

        # for char in t:
        #     t_dict[char] += 1

        return s_dict == t_dict

        