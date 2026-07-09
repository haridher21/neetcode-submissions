class Solution:
    def isValid(self, s: str) -> bool:
        l = 0
        d = {'(': 1, '{': 2, '[': 3, ')': 6, '}': 7, ']': 8}
        for i in s:
            if d[i] < 4:
                l  = l * 10 + d[i]
            else:
                if l == 0:
                    return False
                if l % 10 != d[i] - 5:
                    return False
                else:
                    l = l // 10
        if l:
            return False
        return True