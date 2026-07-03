class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r, cap, max_cap = 0, len(heights) - 1, 0, 0
        while l < r:
            cap = min(heights[l], heights[r]) * (r - l)
            if cap > max_cap:
                max_cap = cap
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return max_cap