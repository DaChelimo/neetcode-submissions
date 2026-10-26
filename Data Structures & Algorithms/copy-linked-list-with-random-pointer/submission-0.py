"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Create hashmap of original to copy
        # Loop through original and get's it, its next and its random
        # Return the head of the new list

        mapper = {}
        curr = head
        output = None

        while curr:
            newNode =  Node(curr.val, curr.next, curr.random)
            if not output:
                output = newNode
            mapper[curr] = newNode
            curr = curr.next
        
        curr = output
        while curr:
            newNext = mapper.get(curr.next, None)
            newRandom = mapper.get(curr.random, None)
            curr.next = newNext
            curr.random = newRandom
            curr = curr.next

        return output


        


        

        