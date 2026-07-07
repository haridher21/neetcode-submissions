class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        n = len(nums)
        maxv, maxi = float('-inf'), -1
        for i in range(n - k + 1): #O(NK)
            maxv = float('-inf')
            for j in range(i, i + k):
                maxv = max(maxv, nums[j])
            output.append(maxv)
        return output
        