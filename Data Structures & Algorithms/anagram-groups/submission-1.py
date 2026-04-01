class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        letters = {}
        for s in strs:
            sort = "".join(sorted(s))
            if sort not in letters:
                letters[sort] = []
            letters[sort].append(s)
        return list(letters.values())