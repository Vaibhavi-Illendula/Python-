class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxi=0
        for s in sentences:
            w=s.count(' ')+1
            maxi=max(w,maxi)
        return maxi
        