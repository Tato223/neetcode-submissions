class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counts = Counter(nums)

        for i in nums:
            if counts.get(i, 0) == 1:
                return i