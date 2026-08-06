class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash = dict()
        for i in range(len(nums)):

            hash_target = target - nums[i]

            if hash_target in hash:
                return [hash[hash_target], i]

            hash[nums[i]] = i