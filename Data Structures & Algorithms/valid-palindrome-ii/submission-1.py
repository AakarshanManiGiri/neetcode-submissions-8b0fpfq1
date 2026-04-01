class Solution:
    def validPalindrome(self, s: str) -> bool:
        leftPoint,rightPoint = 0,len(s)-1
        skipCount = 0
        
        while leftPoint < rightPoint:
            if s[leftPoint] == s[rightPoint]:
                leftPoint += 1
                rightPoint -= 1
            else:
                return self.is_Palindrome(s,leftPoint + 1,rightPoint) or self.is_Palindrome(s,leftPoint,rightPoint - 1)
        return True
    def is_Palindrome(self,s,leftPoint,rightPoint):
        while leftPoint < rightPoint:
            if s[leftPoint] != s[rightPoint]:
                return False
            leftPoint += 1
            rightPoint -= 1
        return True

        