class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        # print(nums)
        while l < r:
            mid = l + ((r - l) // 2)
            # print(l, mid, r, "values", nums[l], nums[mid], nums[r])
            if nums[l] > nums[mid] and nums[mid] < nums[r]:
                # print("r shift mid-1")
                r = mid
            elif nums[l] < nums[mid] and nums[mid] > nums[r]:
                # print("l shift mid+1")
                l = mid
            else:
                break
        # print(l, mid, r, "values", nums[l], nums[mid], nums[r])
        return min(nums[l], nums[r])