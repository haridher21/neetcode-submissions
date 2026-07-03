class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n < 3:
            return 0
        incl, incr, collab = [height[0] for _ in range(n)], [height[n - 1] for _ in range(n)], []
        maxl, maxr = height[0], height[n - 1]
        print(height)
        for i in range(1, n):
            if height[i] > maxl:
                maxl = height[i]
            incl[i] = maxl
        print(incl)
        for i in range(n - 1, 0, -1):
            if height[i] > maxr:
                maxr = height[i]
            incr[i] = maxr
        print(incr)
        for i in range(n):
            collab.append(min(incl[i], incr[i]))
        print(collab)
        total = 0
        for i in range(n):
            print(i, max(collab[i] - height[i], 0))
            total += max(collab[i] - height[i], 0)
        return total
