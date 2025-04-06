class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False
        hash = {}
        for num in nums:
            if num not in hash:
                hash[num]=1
            else:
                hash[num]+=1
                return True
        return False
