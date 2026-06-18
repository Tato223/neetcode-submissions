class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counts = Counter(nums)

        for i in nums:
            if counts.get(i, 0) > 1:
                return True
        return False
