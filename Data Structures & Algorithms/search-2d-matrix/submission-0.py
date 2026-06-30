class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for i in range(len(matrix)):
            low, high = 0, len(matrix[i]) - 1

            while low <= high:
                mid = (low + high) // 2

                if target == matrix[i][mid]:
                    return True
                elif target < matrix[i][mid]:
                    high = mid - 1
                else:
                    low = mid + 1

        return False