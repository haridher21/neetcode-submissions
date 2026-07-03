class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n < 3:
            return 0
        incl, incr, collab = [0 for _ in range(n)], [0 for _ in range(n)], []
        maxl, maxr = height[0], height[n - 1]
        total = 0
        for i in range(n):
            if height[i] > maxl:
                maxl = height[i]
            incl[i] = maxl
            if height[n - i - 1] > maxr:
                maxr = height[n - i - 1]
            incr[n - i - 1] = maxr
        for i in range(n):
            total += max(min(incl[i], incr[i]) - height[i], 0)
        return total
