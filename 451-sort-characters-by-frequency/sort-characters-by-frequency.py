class Solution:
    def frequencySort(self, s: str) -> str:
        d=Counter(s)
        n_s=sorted(d.items(),key=lambda x:-x[1])
        res=''
        for key,value in n_s:
            for _ in range(value):
                res+=key
        return res
        
        