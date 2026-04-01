class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #given integer array nums and target int:
        enum = {}
        for i,n in enumerate(nums):
            compliment = target - n
            if compliment in enum:
                return [enum[compliment],i]
            enum[n] = i