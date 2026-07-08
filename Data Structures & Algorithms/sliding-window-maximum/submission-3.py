class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        nums = [nums[i] * -1 for i in range(n)]
        output, heap = [], []
        for i in range(k):
            heap.append([nums[i], i])
        heapq.heapify(heap)

        for i in range(k, n):
            output.append(heap[0][0])
            while len(heap) and heap[0][1] <= i - k:
                heapq.heappop(heap)
            heapq.heappush(heap, [nums[i], i])
        output.append(heap[0][0])
        output = [output[i] * -1 for i in range(len(output))]
        return output