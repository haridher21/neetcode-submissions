class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod1 = [1 for _ in nums]
        prod2 = [1 for _ in nums]
        n = len(nums)
        i = 1
        while i < n:
            prod1[i] = prod1[i - 1] * nums[i - 1]
            i += 1
        print(prod1)
        i = n - 2
        while i > -1:
            prod2[i] = prod2[i + 1] * nums[i + 1]
            i -= 1
        print(prod2)
        return [prod1[i] * prod2[i] for i in range(n)]