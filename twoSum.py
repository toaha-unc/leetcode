class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return []
        
        hash = {}

        for index, num in enumerate(nums):
            remaining = target - num
            if remaining in hash:
                return [index, hash[remaining]]
            else:
                hash[num] = index
        return []
