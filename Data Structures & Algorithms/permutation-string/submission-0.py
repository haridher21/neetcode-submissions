class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False

        d1, d2 = {}, {}
    
        for i in s1:
            if i in d1:
                d1[i] += 1 
            else:
                d1[i] = 1

        for i in range(n1):
            if s2[i] in d2:
                d2[s2[i]] += 1
            else:
                d2[s2[i]] = 1

        if d1 == d2:
            return True

        for i in range(n1, n2):
            l, r = s2[i - n1], s2[i]
            d2[l] -= 1
            if d2[l] == 0:
                del d2[l]
            if r in d2:
                d2[r] += 1
            else:
                d2[r] = 1
            if d1 == d2:
                return True
        return False
