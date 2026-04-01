class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #given integer array nums and target int:
        number = {}
        for index,value in enumerate(nums):
            compliment = target - value
            if compliment in number:
                return [number[compliment],index]
            number[value] = index
        