class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nr, nc = len(matrix), len(matrix[0])
        tr, br = 0, nr - 1
        while br - tr > 1:
            mr = tr + ((br - tr) // 2)
            # print(tr, mr, br)
            if matrix[mr][0] >= target:
                br = mr
            elif matrix[mr][0] <= target:
                tr = mr
        # print("Check if target is in row:", tr, "and that ",matrix[br][0], "is greater than the target")
        if matrix[tr][0] == target or matrix[br][0] == target:
            return True
        l, r = 0, nc - 1
        if matrix[br][0] < target:
            fr = br
        else:
            fr = tr
        while l <= r:
            mc = l + ((r - l) // 2)
            if matrix[fr][mc] == target:
                return True
            elif matrix[fr][mc] > target:
                r = mc - 1
            else:
                l = mc + 1
        return False
        