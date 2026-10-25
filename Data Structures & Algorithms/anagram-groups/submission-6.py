class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
                # if c not in res:
                #     charDict[c] = 1
                # else:
                #     charDict[c] += 1
            res[tuple(count)].append(s)
            # if charDict not in res:
            #     res[charDict] = [s]
            # else:
            #     res[charDict].append(s)        
        return list(res.values())