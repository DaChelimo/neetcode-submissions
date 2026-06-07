class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Check the length of both strings

        # Dict for s
        # Dict for t

        if (len(s) != len(t)):
            return False

        s_dict = {}
        t_dict = {}

        for char in s:
            s_dict[char] = s_dict.get(char, 0) + 1
            
        for char in t:
            t_dict[char] = t_dict.get(char, 0) + 1


        if (len(s_dict) != len(t_dict)):
            return False

        for k, v in s_dict.items():
            t_value = t_dict.get(k, None)

            if (t_value is None):
                return False
            

            if (t_value != v):
                return False
        
        return True

            


        