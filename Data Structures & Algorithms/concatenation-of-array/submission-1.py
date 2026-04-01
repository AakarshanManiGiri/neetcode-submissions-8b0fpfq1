class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        numLen = len(nums)
        ans = [0] * (2*numLen)
        for index,number in enumerate(nums):
            ans[index] = ans[index + numLen] = number
        return ans
        