def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        
        
        l , r = 0, len(matrix)-1

        while l<=r:
            mid = (l+r)//2
            if matrix[mid][0] == target or matrix[mid][-1] == target:
                return True
            elif matrix[mid][-1] >= target and matrix[mid][0] <= target:
                break
            elif matrix[mid][-1] > target:
                r = mid -1
            else:
                l = mid +1
        
        targetRow = matrix[mid]

        l , r = 0, len(targetRow)-1

        print(mid)

        while l<=r:
            mid = (l+r)//2
            if targetRow[mid] == target:
                return True
            elif targetRow[mid] > target:
                r = mid -1
            else:
                l = mid +1
        return False
