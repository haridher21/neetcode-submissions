class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums = [-i for i in nums]
        heapq.heapify(nums)
        i = 1
        popped = None
        while len(nums) and i < k:
            i += 1
            popped = heapq.heappop(nums)
        if len(nums):
            return -nums[0]
        else:
            return -popped
