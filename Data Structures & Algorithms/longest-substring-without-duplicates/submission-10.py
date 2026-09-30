from collections import defaultdict

class Solution:
    # 1. Create a default dict (value init to 0) (key -> char, value -> num of appearances [capped at 1 for no duplicate]), left, right, max
    # 2. Iterate through string, use if to check if value is == 0 in dict. Add 1 to that value, update max if right -  left is greater than max
    # 3. If not, use while, and in each iteration, move the left pointer while decreasing its value in the dict. Loop ends when the value is now 0, so that we can add over value

# abcdefgf
    # Time: O(n). Space: O(m)
    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     seen = defaultdict(int)

    #     left, right = 0, 0
    #     max_length = 0

    #     while right < len(s):
    #         curr = s[right]

    #         while seen[curr] > 0:
    #             prev = s[left]
    #             seen[prev] -= 1
    #             left += 1
            
    #         # Guaranteed that seen[right] == 0, hence no duplicates between left and right
    #         seen[curr] += 1
    #         max_length = max(max_length, right - left + 1)
    #         right += 1
        
    #     return max_length



    # Seen stores the char and the index
    # Instead of checking count, we check membership and update accordingly

    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}

        left, right = 0, 0
        max_length = 0

        while right < len(s):
            curr = s[right]

            if curr in seen:
                left = max(left, seen[curr] + 1)
                seen[curr] = right
            else:
                seen[curr] = right
            
            max_length = max(max_length, right - left + 1)
            right += 1
        
        return max_length


        