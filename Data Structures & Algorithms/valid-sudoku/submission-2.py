from collections import defaultdict

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
    # def isValidSudoku(self, board: List[List[str]]) -> bool:
    #     for row in board:
    #         tracker = [0] * 10
            
    #         for num in row:
    #             if num == ".":
    #                 continue
    #             num = int(num)

    #             if num != "." and tracker[num] == 1:
    #                 return False
    #             tracker[num] = 1
        
    #     for column in range(9):
    #         tracker = [0] * 10

    #         for row in range(9):
    #             num = board[row][column]
    #             if num == ".":
    #                 continue
    #             num = int(num)

    #             if tracker[num] == 1:
    #                 return False
    #             tracker[num] = 1
        
    #     for i in range(3):
    #         for j in range(3):
    #             startRow = 3 * i # 0, 3, 6
    #             startColumn = 3 * j # 0, 3, 6
                
    #             tracker = [0] * 10

    #             for inner_i in range(startRow, startRow + 3):
    #                 for inner_j in range(startColumn, startColumn + 3):
    #                     num = board[inner_i][inner_j]
    #                     if num == ".":
    #                         continue
    #                     num = int(num)
                        
    #                     if tracker[num] == 1:
    #                         return False
    #                     tracker[num] = 1
                

    #     return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_tracker = defaultdict(lambda: [0] * 10) # Dict where key -> row: value -> array from 0 to 9
        col_tracker = defaultdict(lambda: [0] * 10) # Dict where key -> col: value -> array from 0 to 9
        square_tracker = defaultdict(lambda: [0] * 10) # Dict where key -> (startRow, startCol): 
    #                                      value -> array from 0 to 9

        for row in range(len(board)):
            for col in range(len(board[0])):
                value = board[row][col]

                if value == ".":
                    continue

                value = int(value)

                # Check row
                row_array = row_tracker[row]
                if row_array[value] == 1:
                    return False
                row_array[value] = 1
                
                # Check column
                col_array = col_tracker[col]
                if col_array[value] == 1:
                    return False
                col_array[value] = 1

                # Check square
                startRow = row // 3
                startCol = col // 3
                square_array = square_tracker[(startRow, startCol)]

                if square_array[value] == 1:
                    return False
                square_array[value] = 1

    
        return True
        