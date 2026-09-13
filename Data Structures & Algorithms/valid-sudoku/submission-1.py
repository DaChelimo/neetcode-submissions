class Solution:
    # Given: The board has 9 rows and 9 columns (with digit or . signifying empty)
    # Approach:
    # Loop through every row in every column and check for duplicates 
    #     (how: create a array of 0 to 9 filled with 0s. When a value is seen, update the
    #       corresponding position to be 1. In check phase, if (array[num] == 1), duplicate
    #       exists and return false)
    # TIME: O(1)
    # Similarly, loop through every column and check for duplicates
    # Time: O(1)

    # For i in range(3)
    #   For j in range(3)
    #     window = nums[i, j]
    #       Check inside the window
    #       Make array for checking duplicates
    #       Return if duplicates
    # Time: O(1)

    # Time: O(1). Space: O(1)
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            tracker = [0] * 10
            
            for num in row:
                if num == ".":
                    continue
                num = int(num)

                if num != "." and tracker[num] == 1:
                    return False
                tracker[num] = 1
        
        for column in range(9):
            tracker = [0] * 10

            for row in range(9):
                num = board[row][column]
                if num == ".":
                    continue
                num = int(num)

                if tracker[num] == 1:
                    return False
                tracker[num] = 1
        
        for i in range(3):
            for j in range(3):
                startRow = 3 * i # 0, 3, 6
                startColumn = 3 * j # 0, 3, 6
                
                tracker = [0] * 10

                for inner_i in range(startRow, startRow + 3):
                    for inner_j in range(startColumn, startColumn + 3):
                        num = board[inner_i][inner_j]
                        if num == ".":
                            continue
                        num = int(num)
                        
                        if tracker[num] == 1:
                            return False
                        tracker[num] = 1
                
                print (f"Window Row ({startRow}) to {startRow + 3} || Column ({startColumn} to {startColumn + 3}) is: ")
                print("tracker is ", tracker)
                print(" ")

        return True
        