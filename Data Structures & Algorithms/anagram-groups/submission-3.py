class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lists = []
        indices = {}
        index = 0
        
        for s in strs:
            arranged = str(sorted(s))
            if arranged not in indices:
                indices[arranged] = index
                lists.append([s])
                index += 1
            else:
                if not lists[indices[arranged]]:
                    lists.append([s])
                else:
                    lists[indices[arranged]].append(s)
        
        return lists