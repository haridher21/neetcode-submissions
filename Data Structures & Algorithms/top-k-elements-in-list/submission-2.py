class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for i in nums: # Build freq dict O(N) T S
            d[i] += 1
        
        fd = {}
        for i in d:
            if d[i] in fd:
                fd[d[i]].append(i)
            else:
                fd[d[i]] = [i]
        fkeys = sorted(fd.keys(), reverse=True)
        count, key_ind = 0, 0
        res = []
        while count < k and key_ind < len(fkeys):
            j = 0
            cur_key_len = len(fd[fkeys[key_ind]])
            while count < k and j < cur_key_len:
                res.append(fd[fkeys[key_ind]][j])
                count += 1
                j += 1
            key_ind += 1
        return res
