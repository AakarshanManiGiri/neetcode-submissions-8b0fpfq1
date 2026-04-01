class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbermap = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in numbermap:
                return [numbermap[diff],i]
            numbermap[n] = i



        