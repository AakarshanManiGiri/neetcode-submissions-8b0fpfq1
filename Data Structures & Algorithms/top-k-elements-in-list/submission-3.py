class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for n in nums:
            frequency[n] = 1 + frequency.get(n,0)
        arr = []
        for num,freq in frequency.items():
            arr.append([freq,num])
        arr.sort()
        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res
        
##This solution is O(n log n)
        




        