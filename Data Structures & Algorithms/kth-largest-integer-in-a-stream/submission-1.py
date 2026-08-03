class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        n = len(nums)
        heapq.heapify(self.nums)
        for i in range(n - k):
            _ = heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        if len(self.nums) > self.k:
            _ = heapq.heappop(self.nums)
        return self.nums[0]
        
