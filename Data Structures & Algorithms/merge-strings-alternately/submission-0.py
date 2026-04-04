class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        firstPoint, secondPoint = 0, 0
        res = []
        while firstPoint < len(word1) and secondPoint < len(word2):
            res.append(word1[firstPoint])
            res.append(word2[secondPoint])
            firstPoint += 1
            secondPoint+= 1
        res.append(word1[firstPoint:])
        res.append(word2[secondPoint:])
        return "".join(res)