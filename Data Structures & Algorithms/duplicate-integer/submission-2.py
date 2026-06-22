class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        counts = Counter(nums)

        for i in range(len(nums)):

            if counts.get(nums[i], 0) > 1:
                return True

        return False