class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for i in nums:
            frequency[i] = frequency.get(i,0) + 1
        sorted_nums = sorted(frequency,key=lambda i: frequency[i], reverse=True)
        return sorted_nums[:k]
        