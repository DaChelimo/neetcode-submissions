class Solution:

    # Loop through the strs, read the len, and then format as 6#str. 
    # Append that to the str output
    # Time: O(n). Space: O(n)

    # Edge cases: Str with 10+ chars
    def encode(self, strs: List[str]) -> str:
        result = ""
        
        for s in strs:
            result += str(len(s)) + "#" + s
        
        return result


    # # Looping through s using a index
    # # Look at i and i + 1, check if i is #, check if i + 1 is digit
    # # If both true, create substring of length K (string[i + 2, i + 2 + k] )
    # # Add it to a result list
    # # Move index i to ( i + 2 + k)
    # # Time: O(n). Space: O(n)

    # # Edge cases: Empty list of strs -> "" . List with [""] -> "#0". 
    # # WRONG IMPL.
    # def decode(self, s: str) -> List[str]:   
    #     if len(s) == 0:
    #         return []

    #     i = 0
    #     result = []
        
    #     print(s)
        
    #     while i < len(s): 
    #         if (s[i] == '#'):
    #             j = i + 1
                
    #             length = ""
    #             while j < len(s) and s[j] != "#":
    #                 length += s[j]
    #                 j += 1
                
    #             length = int(length)
    #             substring = s[j:j + length]
    #             result.append(substring)

    #             i = j + length
    #         else:
    #             print(f"s[i] is {s[i]}")
    #             i+= 1
        
    #     result.append()
        
    #     return result


    def decode(self, s: str) -> List[str]:   
        if len(s) == 0:
            return []

        i = 0
        result = []
        
        print(s)
        
        while i < len(s): 
            j = i

            while j < len(s) and s[j] != '#':
                j += 1
            
            length = int(s[i:j])

            result.append(s[j + 1: j + 1 + length])
            i = j + 1 + length

        return result
            

