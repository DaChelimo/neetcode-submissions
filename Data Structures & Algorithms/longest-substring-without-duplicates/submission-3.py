class Solution:
    # PLAN:
    # Naive
    # 1. At each character, loop forward until you find a duplicate
    # 2. Once you do, extract the length of that substring 
    # 3. Compare with the max, and replace max accordingly
    # 4. Move to the next character and do the same
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0

        for index in range(len(s)):
            charset = set()
            j = index
            
            while j < len(s) and s[j] not in charset:
                charset.add(s[j])
                j += 1
            
            maxLen = max(maxLen, len(charset))
        
        return maxLen
    
    # PLAN:
    # Optimal
    # 1. Create two pointers: prev and curr
    # 2. Move prev and curr until they are different (to avoid "aaaabcde")
    #    would be moved until prev = a and curr = b
    # 3a. Move curr until duplicate is found
    # 3b. In every iteration, add the char to a set of seen
    # 4. In every iteration, ensure you get the len of substring and update max
    # 4b. Once duplicate is found, move prev until there is no duplicate 
    # 4c. In every prev, remove the elem from seen
    def lengthOfLongestSubstring(self, s: str) -> int:
        prev = 0
        curr = 1


        if len(s) < 2:
            return len(s)

        while curr < len(s) and s[prev] == s[curr]:
            prev += 1
            curr += 1
        
        if curr == len(s):
            return 1

        maxLen = 0
        seen = set()
        seen.add(s[prev])
        # seen.add(s[curr])

        while curr < len(s):
            char = s[curr]
            
            while char in seen:
                seen.remove(s[prev])
                prev += 1
            
            seen.add(char)
            curr += 1
            maxLen = max(maxLen, curr - prev)
            
        
        maxLen = max(maxLen, curr - prev)
        return maxLen






