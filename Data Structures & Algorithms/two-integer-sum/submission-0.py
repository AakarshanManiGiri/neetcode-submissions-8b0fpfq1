class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {}
        for i,x in enumerate(nums):
            needed = target - x
            if needed in mapping:
                return [mapping[needed],i]
            mapping[x] = i

        
        