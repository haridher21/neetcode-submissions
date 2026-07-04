class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        longest = 0 if n < 1 else 1
        if len(set(s)) == n:
            return n

        l, r = 0, 1
        st = s[l]
        d = {}
        d[s[l]] = l
        while r < n: #O(N) TS
            print(l, r, d, longest)
            if s[r] not in d:
                longest = max(longest, r - l + 1)
            else:
                previous_index = d[s[r]]
                while l < previous_index + 1:
                    del d[s[l]]
                    l += 1
            d[s[r]] = r
            r += 1
        return longest

            
