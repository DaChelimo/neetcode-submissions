class Solution:
    # 1. Use binary search on the first column index of every row
    # 2. Use binary search on the selected row to find target
    # 3. Return true if found, else false

    # Time: O(lg n) + O(lg m) = O(lg (m + n)). Space: O(1)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowStart, rowEnd = 0, len(matrix) - 1
        
        rows = len(matrix)
        columns = len(matrix[0])

        while rowStart <= rowEnd:
            middleRow = (rowStart + rowEnd) // 2

            start = matrix[middleRow][0]
            end = matrix[middleRow][columns - 1]

            if target == start or target == end:
                return True
            
            if target < start:
                rowEnd = middleRow - 1
            elif target > end:
                rowStart = middleRow + 1
            else: # In the middle row, explore it using BS
                colStart, colEnd = 0, columns - 1
            
                while colStart <= colEnd:
                    middleCol = (colStart + colEnd) // 2
                    middle = matrix[middleRow][middleCol]

                    if target == middle:
                        return True
                    elif target < middle:
                        colEnd = middleCol - 1
                    else:
                        colStart = middleCol + 1
                
                break;
        
        return False

                