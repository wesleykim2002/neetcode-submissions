class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            print("r: "+str(r))
            print("prev l: "+str(l))
            while s[r] in charSet:
                print(charSet)
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            print("l: "+str(l))
            print("res: "+str(res))
            res = max(res, r - l + 1)
        return res