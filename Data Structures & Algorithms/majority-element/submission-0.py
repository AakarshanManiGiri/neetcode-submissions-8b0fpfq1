class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numberFreq = {}
        for number in nums:
            numberFreq[number] = numberFreq.get(number,0) + 1
        return max(numberFreq, key=numberFreq.get)
        