class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sChars = {}
        tChars = {}
        for c in s:
            if c not in sChars:
                sChars[c] = 1
            else:
                sChars[c] += 1
        
        for c in t:
            if c not in tChars:
                tChars[c] = 1
            else:
                tChars[c] += 1
        return sChars == tChars