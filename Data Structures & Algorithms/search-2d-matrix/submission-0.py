class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left=0
        m = len(matrix)
        n = len(matrix[0])
        right = m * n - 1

        while(left<=right):
            mid = left+(right-left)//2
            r=mid//n
            c=mid%n
            val = matrix[r][c]
            if val==target:
                return True
            if val>target:
                right=mid-1
            if val<target:
                left=mid+1
        return False