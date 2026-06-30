class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded = encoded + word + "+U+" if word != "" else encoded + "_" + "+U+"
        print(encoded)
        return encoded
    def decode(self, s: str) -> List[str]:
        strs = s.split("+U+")
        if strs[-1] == "":
            strs.pop()
        print(strs)
        index = 0
        while index < len(strs):
            if strs[index] == "_":
                strs[index] = ""
            index += 1
        print(strs)
        return strs
