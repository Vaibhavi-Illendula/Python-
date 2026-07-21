class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n=len(s)
        m=len(p)
        if m>n:
            return []
        p_count={}
        window={}
        for ch in p:
            if ch in p_count:
                p_count[ch]+=1
            else:
                p_count[ch]=1
        for i in range(m):
            ch=s[i]
            if ch in window:
                window[ch]+=1
            else:
                window[ch]=1
        ans=[]
        if window==p_count:
            ans.append(0)
        for i in range(m,n):
            ch=s[i]
            if ch in window:
                window[ch]+=1
            else:
                window[ch]=1
            left=i-m
            window[s[left]]-=1
            if window[s[left]]==0:
                del window[s[left]]
            if p_count==window:
                ans.append(i-m+1)
        return ans



            
            

        

        