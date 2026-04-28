class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        leftpoint,rightpoint = 0,len(nums)
        while leftpoint < rightpoint:
            midpoint = leftpoint + ((rightpoint-leftpoint)//2)
            if nums[midpoint]>=target:
                rightpoint = midpoint
            elif nums[midpoint]< target:
                leftpoint = midpoint + 1
        return leftpoint

            
            

        