class Solution:

    # INPUT:  str s
    # OUTPUT: bool -> true, 1. (), 2. Correct order. 3. Closing brack <-> Opening brack

    # PLAN:
    # 1. Build a stack: (, {, [
    # 2. Append any new open parans to the stack
    # 3. If we find closing, we try popping (if it matches top of the stack)
    # 4. If closing and does not pop stack, return False .... {[)]}

    # Edge cases: Empty string -> true. 1 char -> False. Same applies to odd
    # Edge cases: "]})))" or "[[("

    # Time: O(n). Space: O(n)
    def isValid(self, s: str) -> bool:
        stack = []
        book = {
            '}': '{',
            ']' : '[',
            ')' : '('
        }

        if len(s) % 2 == 1:
            return False

        for c in s:
            if c in book:
                latest_open = stack.pop() if stack else None
                
                if book[c] != latest_open:
                    return False
            else: 
                stack.append(c)
        
        return False if stack else True
        