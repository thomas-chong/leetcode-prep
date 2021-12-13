class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1
        while i <= j:
            q = (i + j) // 2
            if nums[q] == target:
                return q
            elif nums[q] > target:
                j = q - 1
            else:
                i = q + 1
        if target > nums[q]:
            return q + 1
        else:
            return q