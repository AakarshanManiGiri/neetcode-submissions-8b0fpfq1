class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS,countT = {},{}
        for ltr in range(len(s)):
            countS[s[ltr]] = 1 + countS.get(s[ltr],0)
            countT[t[ltr]] = 1 + countT.get(t[ltr],0)
        return countS == countT
        
        

        