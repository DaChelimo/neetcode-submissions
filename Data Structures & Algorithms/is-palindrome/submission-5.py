class Solution:

    # INPUT: str s
    # OUTPUT: bool

    # Constraints: Remove spaces, and all other punctuation. IGNORE CASE.
    # Edge Cases: Str with 0, 1 chars -> Palindrome

    # APPROACH 1:
    # 1. Loop through s, and create an arr letters with valid chars
    # 2. Loop through the arr, with two indicies start and end
    # 3. If they get together or overlap, return True
    # 4. Otherwise (if it stops along the way), return False

    # Time: O(n). Space: O(n)
    def isPalindrome(self, s: str) -> bool:
        if len(s) < 2:
            return True
 
        letters = []
        for c in s:
            if c.isalnum():
                letters.append(c.lower())
        
        start = 0
        end = len(letters) - 1

        while start < end:
            if letters[start] != letters[end]:
                print(f"letters[start] is {letters[start]} and letters[end] is {letters[end]}")
                return False
            
            start += 1
            end -= 1
        
        return True
            
        