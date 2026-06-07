class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanup = []

        for char in s:
            if (char.isalnum()):
                cleanup.append(char)

        sizeOfCleanup = len(cleanup)
        
        for i in range(sizeOfCleanup):
            forwardChar = cleanup[i].lower()
            backwardChar = cleanup[sizeOfCleanup - 1 - i].lower()

            if (forwardChar != backwardChar):
                return False
            
            if (i == (sizeOfCleanup / 2 + sizeOfCleanup % 2)):
                return True

        return True