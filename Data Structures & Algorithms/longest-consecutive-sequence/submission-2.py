class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = defaultdict(int)
        n = len(nums)
        for i in range(n):
            d[nums[i]] = i

        starters = []
        for i in range(n):
            if nums[i] - 1 not in d:
                starters.append(nums[i])

        print(starters)
        
        max_count = 0
        for starter in starters:
            element = starter
            count = 1
            while element + 1 in d:
                count += 1
                element += 1

            if count > max_count:
                max_count = count

        return max_count