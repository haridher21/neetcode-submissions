class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        for i in tasks:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

        q, qs, qf = [None] * n, 0, {}
        cycles = 0
        while len(freq):
            cycles += 1

            mf, mft = 0, None
            for i in freq:
                if i not in qf and freq[i] > mf:
                    mf = freq[i]
                    mft = i

            if q[qs]:
                del qf[q[qs]]
            qs += 1
            
            if mft is None:
                q.append(None)
                continue
            q.append(mft)
            qf[mft] = True

            freq[mft] -= 1
            if freq[mft] == 0:
                del freq[mft]

        return cycles

                
            
        