class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l, d = [], {}
        for word in strs:
            copy = list(word)
            copy.sort()
            copy = "".join(copy)
            if copy in d:
                d[copy].append(word)
            else:
                d[copy] = [word]
        for i in d:
            l.append(d[i])
        return l