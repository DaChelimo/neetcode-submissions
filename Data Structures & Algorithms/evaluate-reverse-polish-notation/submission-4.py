import math

class Solution:
    # Constraints: 
    # a) List of operations -> NOt possible; 
    # b) One operation only -> Execute and return result
    # c) Plain numbers -> Not possible
    # d) Is "1, +, 2" -> Not Possible

    # PLAN:
    # 1. Create a stack (keep track of the numbers we have seen)
    # 2. Loop through the tokens, add the numbers to the top of stack
    # 3. If x is an operator, pop the last two numbers (guaranteed)
    # 4. Do operation, and push the result onto the stack
    #  5. Continue with the loop

    # Time: O(n). Space: O(n)
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        symbols = {'+': add, '-': minus, '*': multiply, '/': div}

        for token in tokens:
            if token in symbols:
                second = stack.pop()
                first = stack.pop()

                result = symbols[token](first, second)
                stack.append(result)

            else:
                stack.append(int(token))


        return stack[-1]

def add(a: int, b: int) -> int:
    return a + b

def minus(a: int, b: int) -> int:
    return a - b

def multiply(a: int, b: int) -> int:
    return a * b

def div(a: int, b: int) -> int:
    return math.trunc(a / b)

                


        