class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d, dgram, result = {}, {}, []
        BETS = "abcdefghijklmnopqrstuvwxyz"
        for c in BETS: #INIT
            d[c] = 0

        for word in strs:
            for c in d: #RESET
                d[c] = 0

            for c in word: #Collect Frequencies
                if c in d:
                    d[c]+=1
                else:
                    d[c]

            ana = ""
            for c in BETS: #Build sorted anagram
                ana += (c * d[c])
            if ana in dgram:
                dgram[ana].append(word)
            else:
                dgram[ana] = [word]
        for ana in dgram:
            result.append(dgram[ana])
        return result