class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        arrLen = len(nums)
        newLen = len(nums) * 2
        ans = [0] * newLen

        for i in range(arrLen):
            ans[i] = nums[i]
            ans[i + arrLen] = nums[i]

        return ans