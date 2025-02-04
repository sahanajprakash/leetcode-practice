class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        first = strs[0]
        last = strs[-1]

        minL = min(len(first), len(last))

        i=0

        while i<minL and first[i] == last[i]:
            i+=1
        
        return first[:i]

        