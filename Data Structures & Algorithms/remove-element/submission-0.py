class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        counter = 0
        numLen = len(nums)
        while counter < numLen:
            if nums[counter] == val:
                numLen -= 1
                nums[counter] = nums[numLen]
            else:
                counter += 1
        return numLen

        