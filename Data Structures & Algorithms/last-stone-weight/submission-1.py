class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [stones[i] * -1 for i in range(len(stones))]
        heapq.heapify(stones)
        while len(stones) > 1:
            heavy = heapq.heappop(stones)
            light = heapq.heappop(stones)
            diff = heavy - light
            if diff:
                heapq.heappush(stones, diff)
        return stones[0] * -1 if len(stones) else 0