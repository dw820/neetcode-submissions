class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m = len(matrix)
        n = len(matrix[0])

        l = 0
        r = m - 1
        
        while l < r:
            mid = (l + r) // 2 + 1

            if matrix[mid][0] < target:
                l = mid
            elif matrix[mid][0] > target:
                r = mid - 1
            else:
                return True


        l_row = 0
        r_row = n - 1

        while l_row <= r_row:
            mid = (l_row + r_row) // 2

            if matrix[l][mid] < target:
                l_row = mid + 1
            elif  matrix[l][mid] > target:
                r_row = mid - 1
            else:
                return True
        

        return False
            

