class Solution:
    def minWindow(self, s: str, t: str) -> str:
        sn, tn = len(s), len(t)
        if tn > sn:
            return ""
        dt, ds = {}, {}
        unique_matches = 0
        required_matches = 0

        best_indices = []
        shortest = 0


        for i in t:
            dt[i] = 1 + dt.get(i, 0)
        required_matches = len(dt)

        l, r = 0, 0
        while r < sn: #O(N) T #O(M) S
            if unique_matches == required_matches:
                if shortest:
                    if shortest > (r - l + 1):
                        shortest = r - l + 1
                        best_indices = [l, r]
                else:
                    shortest = r - l + 1
                    best_indices = [l, r]

                if shortest == 1:
                    break

                # Now increase l until its the smallest current substring
                if s[l] in dt:
                    ds[s[l]] = ds[s[l]] - 1 if ds[s[l]] > 1 else 0
                    if ds[s[l]] < dt[s[l]]: #Not matching anymore
                        unique_matches -= 1
                        r += 1
                l += 1

            elif unique_matches != required_matches:
                if s[r] in dt:
                    ds[s[r]] = 1 + ds.get(s[r], 0)
                    if ds[s[r]] == dt[s[r]]:
                        unique_matches += 1
                        if unique_matches == required_matches:
                            continue
                r += 1
    
        if shortest:
            return s[best_indices[0] : best_indices[1] + 1]
        else:
            return ""
