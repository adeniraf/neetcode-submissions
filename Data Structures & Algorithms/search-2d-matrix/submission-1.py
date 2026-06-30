class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for i in range(0, len(matrix)):
            low, high = 0, len(matrix[i]) - 1

            # if the target is not in the current subarray
            # move to next iteration/subarray
            if target > matrix[i][high]:
                continue
            # else, we have found the sub-array to search in
            # perform Binary Search
            while low <= high:
                mid = (low + high) // 2
                if target == matrix[i][mid]:
                    return True
                elif target > matrix[i][mid]:
                    low = mid + 1
                else:
                    high = mid - 1
        return False
        