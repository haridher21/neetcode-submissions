class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        longest = 0 if len(s) == 0 else 1
        for l in range(n - 1):
            for r in range(l + 1, n + 1):
                st = s[l : r]
                sst = set(st)
                length = len(st)
                if length != len(sst):
                    continue
                longest = max(longest, length)
        return longest

