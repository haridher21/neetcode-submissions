class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() #NLogN
        n = len(nums)
        l, r = 0, n - 1
        d = {}
        for f in range(0, n - 2): #O(N^2)
            l, r = f + 1, n - 1
            while l < r:
                sum = nums[f] + nums[l] + nums[r]
                if sum == 0:
                    d[(nums[f], nums[l], nums[r])] = True
                    l += 1
                    r -= 1
                elif sum > 0:
                    r -= 1
                else:
                    l += 1
        return list(d.keys())