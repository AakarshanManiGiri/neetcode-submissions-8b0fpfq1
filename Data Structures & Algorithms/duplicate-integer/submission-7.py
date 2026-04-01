class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #int array nums
        #return true if value appears more than once else false
        num = set()
        for n in nums:
            if n in num:
                return True
            num.add(n)
        return False