class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #int array nums
        #return true if value appears more than once else false
        num = set()
        for i in nums:
            if i in num:
                return True
            num.add(i)
        return False
            