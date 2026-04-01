class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #given strings s,t
        #to return true if theyre anagrams else false
        if len(s) != len(t):
            return False
        letterS,letterT = {},{}
        for index in range(len(s)):
            letterS[s[index]] = letterS.get(s[index],0) + 1
            letterT[t[index]] = letterT.get(t[index],0) + 1
        return letterS == letterT