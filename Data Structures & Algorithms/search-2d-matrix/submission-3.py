class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def searchRow():
            l = 0
            r = len(matrix) - 1
            while l <= r:
                m = (r-l)//2 + l
                if matrix[m][0] <= target <= matrix[m][len(matrix[m])-1]:
                    return m
                elif target < matrix[m][0]:
                    r = m - 1
                else:
                    l = m + 1

            return -1
        
        row = searchRow()

        if row < 0:
            return False

        def binarySearch():
            l = 0
            r = len(matrix[row]) - 1
            while l <= r:
                m = (r-l)//2 + l
                if target == matrix[row][m]:
                    return True
                elif target < matrix[row][m]:
                    r = m - 1
                else:
                    l = m + 1

            return False

        return binarySearch()