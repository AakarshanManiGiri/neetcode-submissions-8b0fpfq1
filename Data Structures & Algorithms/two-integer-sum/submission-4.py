class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #given integer array nums and target int:
        number = {}
        for i,n in enumerate(nums):
            compliment = target - n
            if compliment in number:
                return [number[compliment], i]
            number[n] = i