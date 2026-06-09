class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        D = {}
        for w in strs:
            word = list(w)
            word.sort()
            # word = str(word)
            d = {}
            for i in word:
                if i in d:
                    d[i] += 1
                else:
                    d[i] = 1
            st = ""
            for c in d:
                st += c + str(d[c])
            if st in D:
                D[st].append(w)
            else:
                D[st] = [w]
        l = []
        print(D)
        for st in D:
            l.append(D[st])
        return l
            