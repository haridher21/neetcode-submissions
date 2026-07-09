class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        d = {'(': ')', '{': '}', '[': ']'}
        for i in s:
            print(i, l)
            if i in d:
                l.append(i)
            else:
                if len(l) == 0:
                    return False
                if d[l[-1]] != i:
                    return False
                else:
                    l.pop()
        if len(l):
            return False
        return True