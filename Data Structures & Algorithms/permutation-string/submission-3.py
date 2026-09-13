from collections import Counter, defaultdict

class Solution:
    # Input: two strings 
    # Output: True if that is true (s1 is a substring + permutation of s2)). False otherwise

    # Plan:
    # 1. Create a counter from s1
    # 1b) Create two pointers: start and end
    # 2. Build a set of seen chars 
    # 3. Loop through s2 (using end)
    #   a) Check if seen == s1.counter(). If so, return true
    #   b) Check if the char at i is in seen (and char is at it's target capacity), meaning we have encountered a duplicate ... or, we find a char that is not in s1
    #   b - ii) Move the start pointer until the duplicate is no longer there .. or, the unwanted char is no longer there
    
    #   c) Else: Check if the char is in s1. If so, add to the seen char
    #   d) Move the pointer forward
    # 4. If pointer reaches the end, return false

    # Edge Cases: 
    # 1. s1 empty -> return true
    # 2. s2 len < s1 len -> false (cannot be substring of a smaller string)
    # 3. s2 len < 2 -> return s2 == s1

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) == 0:
            return True
        elif len(s2) < len(s1):
            return False
        elif len(s1) == len(s2):
            return set(s1) == set(s2)
    

        seen = defaultdict(int) # dict (key - char, value - occurrences)
        s1_count = Counter(s1)
        start, end = 0,0 # Tracking movement in s2

        print("s1_count is ", s1_count)

        while end < len(s2):
            print("Seen is ", seen)
            print("")
            
            if (seen == s1_count):
                return True
            
            # aabc -> a: 2 laabac
            curr = s2[end]
            if (curr in s1_count):
                seen[curr] += 1

                while seen[curr] > s1_count[curr] and start <= end:
                    start_char = s2[start]
                    seen[start_char] = max(seen[start_char] - 1, 0)
                    start += 1
            else:
                start = end
                seen.clear()

            end += 1
        

        
        return seen == s1_count




        