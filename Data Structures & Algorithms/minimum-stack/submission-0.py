# CONSTRAINTS: pop, top, getMin on non-empty stacks
# Can we have duplicates: push(0)... push(0)
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        add_to_min_stack = len(self.min_stack) == 0 or val <= self.min_stack[-1]

        if (add_to_min_stack):
            self.min_stack.append(val)
        
    def pop(self) -> None:
        removed_item = self.stack.pop()

        if (removed_item == self.min_stack[-1]):
            self.min_stack.pop()


    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.min_stack[-1]

        
