class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort() #O(NlogN)
        if len(nums) <= 1:
            return len(nums)
        cur_len, max_len = 1, 1
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] == 1:
                cur_len += 1
                if cur_len > max_len:
                    max_len = cur_len
            elif nums[i] == nums[i - 1]:
                continue
            else:
                cur_len = 1
        return max_len
        