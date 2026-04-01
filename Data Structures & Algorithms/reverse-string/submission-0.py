class Solution:
    def reverseString(self, s: List[str]) -> None:
        leftPoint,rightPoint = 0 , len(s)-1
        while leftPoint < rightPoint:
            s[leftPoint],s[rightPoint] = s[rightPoint],s[leftPoint]
            leftPoint += 1
            rightPoint -= 1
        return s

        