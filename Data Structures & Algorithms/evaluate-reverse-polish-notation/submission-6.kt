import kotlin.math.truncate

class Solution {
   
    // REMEMBER: 
    // 1. Division should be rounded towards 0
    // 2. Just a single number and no operation e.g ["10"]
   
    // PLAN:
    // # 1. Create a stack (keep track of the numbers we have seen)
    // # 2. Loop through the tokens, add the numbers to the top of stack
    // # 3. If x is an operator, pop the last two numbers (guaranteed)
    // # 4. Do operation, and push the result onto the stack
    // #  5. Continue with the loop
    
    fun evalRPN(tokens: Array<String>): Int {
        val stack = mutableListOf<Int>()
        val operations = hashMapOf<String, (Int, Int) -> Int>(
            "+" to ::add,
            "-" to ::minus,
            "*" to ::multiply,
            "/" to ::divide,
        )

        for (token in tokens) {
            if (operations.contains(token)) {
                val second = stack.removeLast()
                val first = stack.removeLast()
        
                val result = operations.getValue(token)(first, second)
                stack.add(result)
            } 
            else stack.add(token.toInt())
        }

        return stack.first()
    }

    fun add(a: Int, b: Int): Int = a + b
    fun minus(a: Int, b: Int): Int = a - b
    fun multiply(a: Int, b: Int): Int = a * b
    fun divide(a: Int, b: Int): Int = truncate(a.toDouble() / b.toDouble()).toInt()

}
