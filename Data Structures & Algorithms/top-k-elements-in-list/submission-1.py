class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for i in nums: # Build freq dict O(N) T S
            d[i] += 1
        freq_list, res = [], []
        for i in d: # Make a list out of it, with freq as first element
            freq_list.append([d[i], i]) # O(N) TS worst case
        freq_list.sort(reverse=True) # Sort O(N log N) worst case
        freq_list = freq_list[:k] # Top k
        for i in freq_list: # Extract the second integer element
            res.append(i[1]) # O(K)
        return res